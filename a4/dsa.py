'''
    The script to implement DSA.
'''

from random import randint

import hashlib
from math_helper import *

class Dsa:

    def __init__(self, p, q, g, hash=hashlib.sha1):
        self.p = p
        self.q = q
        self.g = g
        self.hash = hash
        self.update_k_and_r()

    def key_gen(self):
        private_key = randint(1, self.q - 1)
        public_key = fast_pow(self.g, private_key, self.p)
        return (private_key, public_key)

    def update_k_and_r(self):
        self.k = randint(1, self.q - 1)
        self.k_inv, _ = extgcd(self.k, self.q)
        self.k_inv %= self.q
        self.r = fast_pow(self.g, self.k, self.p) % self.q

    def sign(self, m: int, private_key: int):
        m_hash = int(self.hash(m.to_bytes(self.q.bit_length(), 'big')).hexdigest(), 16) % self.q
        # print(f"sign: m_hash = {m_hash}") # debug
        s = ((m_hash + private_key * self.r) * self.k_inv) % self.q
        return (self.r, s)

    def verify(self, m: int, r: int, s: int, public_key: int):
        m_hash = int(self.hash(m.to_bytes(self.q.bit_length(), 'big')).hexdigest(), 16) % self.q
        # print(f"verify: m_hash = {m_hash}") # debug
        s_inv, _ = extgcd(s, self.q)
        s_inv %= self.q
        u1 = (m_hash * s_inv) % self.q
        u2 = r * s_inv % self.q
        cksum = (fast_pow(self.g, u1, self.p) * fast_pow(public_key, u2, self.p)) % self.p % self.q
        return cksum == r
