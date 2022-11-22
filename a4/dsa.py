'''
    The script to implement DSA.
'''

from random import randint

import hashlib
from math_helper import *

class Dsa:

    def __init__(self, p, q, g):
        self.p = p
        self.q = q
        self.g = g
        self.k = randint(1, self.q - 1)
        self.k_inv, _ = extgcd(self.k, q)

    def key_gen(self):
        self.private_key = randint(1, self.q - 1)
        self.public_key = fast_pow(self.g, self.private_key, self.p)
        return (self.private_key, self.public_key)

    def sign(self, m: str):
        pass
