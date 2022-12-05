from dsa import Dsa
from dsa_num import *
from math_helper import *

if __name__ == "__main__":
    # use SHA1 as the hash function by default as required
    dsa_inst = Dsa(p, q, g)
    x, y = dsa_inst.key_gen()
    # question 2
    q2_m = 522346828557612 # given
    q2_r, q2_s = dsa_inst.sign(q2_m, x)
    q2_verified = dsa_inst.verify(q2_m, q2_r, q2_s, y)
    if q2_verified:
        print("Question 2 signature is verified!")
    else:
        print("Question 2 signature isn't verified...")
    print()

    # question 3
    q3_m = 8161474912883
    # NOTE:
    # Don't call dsa_inst.update_k_and_r() here to use the same k as question 2
    q3_r, q3_s = dsa_inst.sign(q3_m, x)
    q3_verified = dsa_inst.verify(q3_m, q3_r, q3_s, y)
    if q3_verified:
        print("Question 3 signature is verified!")
    else:
        print("Question 3 signature isn't verified...")
    print()
    # try to recover k
    m_hash_diff = (dsa_inst.hash_int(q2_m) - dsa_inst.hash_int(q3_m)) % dsa_inst.q
    s_diff = (q2_s - q3_s) % dsa_inst.q
    s_diff_inv, _ = extgcd(s_diff, dsa_inst.q)
    s_diff_inv %= dsa_inst.q
    k_compromised = (m_hash_diff * s_diff_inv) % dsa_inst.q
    print(f"compromised k = {k_compromised}")
    print(f"original k    = {dsa_inst.k}")
    if k_compromised == dsa_inst.k:
        print("k is compromised!")
    print()
    r_inv, _ = extgcd(dsa_inst.r, dsa_inst.q)
    x_compromised = (k_compromised * q2_s - dsa_inst.hash_int(q2_m)) * r_inv % dsa_inst.q
    print(f"compromised x (private key) = {x_compromised}")
    print(f"original x (private key)    = {x}")
    if x_compromised == x:
        print("x (private key) is recovered using compromised k!")
    print()
