from dsa import Dsa
from dsa_num import *

if __name__ == "__main__":
    # Use SHA1 as the hash function by default as required
    dsa_inst = Dsa(p, q, g)
    # question 2
    q2_x, q2_y = dsa_inst.key_gen()
    q2_m = 522346828557612 # given
    q2_r, q2_s = dsa_inst.sign(q2_m, q2_x)
    q2_verified = dsa_inst.verify(q2_m, q2_r, q2_s, q2_y)
    if q2_verified:
        print("Question 2 signature is verified!")
    else:
        print("Question 2 signature isn't verified...")
