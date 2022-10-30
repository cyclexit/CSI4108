'''
    Elgamal Cryptographic System
'''
import random

q = 89
alpha = 13

# private key
xa = random.randint(2, q - 2)

# public key
ya = (alpha ** xa) % q

def encrypt(q, alpha, ya):
    pass

def decrypt(xa):
    pass
