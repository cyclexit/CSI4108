from random import randint, randrange

from math_helper import *

P_BITS = 1024
Q_BITS = 160
PQ_BIT_GAP = P_BITS - Q_BITS

def write_to_file(p, q, g):
    with open("dsa_num.py") as f:
        f.write("'''\n")
        f.write(f"This file is automated generated by {__file__}.\n")
        f.write("'''\n")
        f.write("p = " + str(p))
        f.write("\n")
        f.write("q = " + str(q))
        f.write("\n")
        f.write("g = " + str(g))
        f.write("\n")

def main():
    while True:
        q = get_prime(Q_BITS)
        k = randrange(1 << (PQ_BIT_GAP - 1), 1 << PQ_BIT_GAP)
        p = k * q + 1
        while not (is_prime(p, 5)) :
            q = get_prime(160)
            k = randrange(1 << (PQ_BIT_GAP - 1), 1 << PQ_BIT_GAP)
            p = k * q + 1
        g = fast_pow(randint(2, p - 1), (p - 1) // q, p)
        if p.bit_length() == P_BITS and fast_pow(g, q, p) == 1:
            write_to_file(p, q, g)

if __name__ == "__main__":
    main()