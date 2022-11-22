'''
    The script to implement DSA.
'''

from random import randint

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

def miller_rabin_test(n: int):
    # corner cases
    if n <= 4:
        if n == 2 or n == 3:
            return False
        return True

    q = n - 1
    k = 0
    while q % 2 == 0:
        k += 1
        q >>= 1
    # 1 < a < (n - 1), i.e., 2 <= a <= (n - 2)
    a = randint(2, n - 2)

    if fast_pow(a, q, n) == 1:
        return False # inconclusive

    e = q
    for _ in range(k):
        if (n - 1) == fast_pow(a, e, n):
            return False # inconclusive
        e <<= 1

    return True # composite

class Dsa:
    # 1024-bit prime generated on https://asecuritysite.com/encryption/getprimen.
    p = 122727601331362196256320614825994745261180084640875573500354145079401305058408145479727474780222062274515656953116192984694653041627428607701888380909829641355178938145822810216707935904997442559170303277526692121365192370068805095986797320862059010969177983287955533113322628977650649119413520055439276236391

    def __init__(self):
        pass
