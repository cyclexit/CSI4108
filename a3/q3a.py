e = 65537 # public key (given)
m = 466921883457309 # (given)

p = 384759392039
q = 3495892748912
n = p * q # public key (given)

def fast_pow(x: int, y: int, n: int):
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

def euler_totient(n: int):
    r = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            r -= r // i
            while n % i == 0:
                n //= i
        i += 1
    r -= r // n
    return r

def main():
    # 0. get the private key
    phi_n = euler_totient(n)
    d, _ = extgcd(e, phi_n) # private key
    d %= phi_n # make sure d is positive
    
    # 1. encrypt m to c
    c = fast_pow(m, e, n)

    # 2. decrypt c with CRT, profile it
    # 3. decrypt c without CRT, profile it

if __name__ == "__main__":
    main()