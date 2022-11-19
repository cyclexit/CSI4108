'''
    Elgamal Cryptographic System
'''
import random

def fast_pow(x, y, n):
    res = 1;
    x = x % n;
    while y > 0:
        if y & 1:
            res = (res * x) % n
        y >>= 1
        x = (x * x) % n
    return res

def extgcd(a: int, b: int):
    if b == 0:
        return (1, 0)
    else:
        y, x = extgcd(b, a % b)
        y -= x * (a // b)
        return (x, y)

q = 89 # (given)
alpha = 13 # (given)

def key_gen():
    # private key
    xa =  random.randint(2, q - 2)
    # public key
    ya = fast_pow(alpha, xa, q)
    return xa, ya

def encrypt(m, q, alpha, ya):
    k = random.randint(1, q - 1)
    K = fast_pow(ya, k, q)
    c1 = fast_pow(alpha, k, q)
    c2 = (K * m) % q
    return c1, c2

def decrypt(c1, c2, xa, q):
    K = fast_pow(c1, xa, q)
    K_inv, _ = extgcd(K, q)
    m = (c2 * K_inv) % q
    return m

def main():
    xa, ya = key_gen()
    print(f"private key: xa = {xa}")
    print(f"public key: q = {q}, alpha = {alpha}, ya = {ya}\n")

    m = random.randint(0, q - 1)
    print(f"plaintext: m = {m}\n")

    c1, c2 = encrypt(m, q, alpha, ya)
    print(f"ciphertext: c1 = {c1}, c2 = {c2}\n")

    m_decrypted = decrypt(c1, c2, xa, q)
    print(f"decrypted plaintext: m_decrypted = {m_decrypted}\n")

    if m == m_decrypted:
        print("Data integrity is verified")
    else:
        print("Data integrity is broken")

if __name__ == "__main__":
    main()
