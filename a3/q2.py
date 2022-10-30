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

def main():
    t = 5
    max_value = (1 << 14) - 1
    # find 14-bit prime numbers
    for num in range(2, max_value + 1):
        is_composite = False
        for _ in range(0, t):
            if miller_rabin_test(num):
                is_composite = True
                break
        if is_composite == False:
            print(num, end=", ")
    print()

if __name__ == "__main__":
    main()
