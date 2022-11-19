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
    MIN_VALUE_14BIT = 1 << 13
    MAX_VALUE_14BIT = (1 << 14) - 1
    # find 14-bit prime numbers
    found = False
    while not found:
        num = randint(MIN_VALUE_14BIT, MAX_VALUE_14BIT)
        print(f"Try the number {num}...")
        is_composite = False
        for _ in range(0, t):
            if miller_rabin_test(num):
                is_composite = True
                break
        if is_composite:
            print(f"Oops, {num} is not 14-bit prime.\n")
        else:
            print(f"Ah ha, {num} is a probably 14-bit prime!")
            found = True

if __name__ == "__main__":
    main()
