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

q = 89 # (given)
alpha = 13 # (given)

# private key
xa = 12 # random.randint(2, q - 2)

# public key
ya = fast_pow(alpha, xa, q)

def encrypt(q, alpha, ya):
    pass

def decrypt(xa):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
