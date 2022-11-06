'''
    References:
    1. https://asecuritysite.com/encryption/ecdh3
'''
import collections
import time
from random import randint

# Copied code starts
EllipticCurve  = collections.namedtuple("EllipticCurve", ["p", "a", "b", "g", "n", "h"])
curve = EllipticCurve(
    p = 115792089210356248762697446949407573530086143415290314195533631308867097853951,
    a = -3,
    b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b,
    g = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5),
    n = 115792089210356248762697446949407573529996955224135760342422259061068512044369,
    h = 1,
)

def inverse_mod(k, p):
    """Returns the inverse of k modulo p.
    This function returns the only integer x such that (x * k) % p == 1.
    k must be non-zero and p must be a prime.
    """
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)

    # Extended Euclidean algorithm.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return x % p

def is_on_curve(point):
    """Returns True if the given point lies on the elliptic curve."""
    if point is None:
        # None represents the point at infinity.
        return True

    x, y = point
    return (y * y - x * x * x - curve.a * x - curve.b) % curve.p == 0

def point_add(point1, point2):
    """Returns the result of point1 + point2 according to the group law."""
    assert is_on_curve(point1)
    assert is_on_curve(point2)

    if point1 is None:
        # 0 + point2 = point2
        return point2
    if point2 is None:
        # point1 + 0 = point1
        return point1

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2 and y1 != y2:
        # point1 + (-point1) = 0
        return None

    if x1 == x2:
        # This is the case point1 == point2.
        m = (3 * x1 * x1 + curve.a) * inverse_mod(2 * y1, curve.p)
    else:
        # This is the case point1 != point2.
        m = (y1 - y2) * inverse_mod(x1 - x2, curve.p)

    x3 = m * m - x1 - x2
    y3 = y1 + m * (x3 - x1)
    result = (x3 % curve.p,
              -y3 % curve.p)

    assert is_on_curve(result)

    return result

def point_neg(point):
    x, y = point
    return (x, -y % curve.p)

def scalar_mult(k, point):
    """Returns k * point computed using the double and point_add algorithm."""
    assert is_on_curve(point)

    if k % curve.n == 0 or point is None:
        return None

    if k < 0:
        # k * point = -k * (-point)
        return scalar_mult(-k, point_neg(point))

    result = None
    addend = point

    while k:
        if k & 1:
            # Add.
            result = point_add(result, addend)

        # Double.
        addend = point_add(addend, addend)

        k >>= 1

    assert is_on_curve(result)

    return result
# Copied code ends

def ecdh_key_gen():
    # Alice's key pair
    na = randint(1, curve.n) # private
    pa = scalar_mult(na, curve.g) # public
    # Bob's key pair
    nb = randint(1, curve.n) # private
    pb = scalar_mult(nb, curve.g) # public

    # Alice's shared secret
    ka = scalar_mult(na, pb)
    # Bob's shared secret
    kb = scalar_mult(nb, pa)
    return na, pa, nb, pb, ka, kb

def main():
    print(curve)
    start_time = time.time_ns()
    na, pa, nb, pb, ka, kb = ecdh_key_gen()
    print(f"ECDH Time: {(time.time_ns() - start_time)} ns")
    pass

if __name__ == "__main__":
    main()
