import time

e = 65537 # public key (given)
m = 466921883457309 # (given)

# p and q are 1024-bit prime numbers generated on https://asecuritysite.com/encryption/getprimen
p = 165400444044747433312445922891272961642467363198542552546815056518492207400410183475876924235244207345582667264212152258884889029091823686598618205716016123976847711571546890139625855461023519130246843957820607537157730941623895113031816296869120611337061836462264221888001352786894176383967235037290836349441
q = 174119558295564641396545869896429065080430412778702047563033362554797540721654305034015906940013233630828507090787295700798765934410631293607422599651923517465262898865502465770953177116144406278037285660891316806898598572536313770725851416924000582846375565373461305303155784370251386514960332483945722073697
n = p * q # public key
phi_n = (p - 1) * (q - 1)

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

def main():
    # 0. get the private key
    d, _ = extgcd(e, phi_n) # private key
    d %= phi_n # make sure d is positive
    
    # 1. encrypt m to c
    c = fast_pow(m, e, n)

    # 2. decrypt c without CRT, profile it
    print("Decrypt c without CRT:")
    start_time = time.time_ns()
    m1 = fast_pow(c, d, n)
    assert(m == m1) # make sure we get the correct plaintext
    print(f"{(time.time_ns() - start_time)} ns")

    # 3. decrypt c with CRT, profile it
    start_time = time.time()
    print("Decrypt c with CRT:")
    start_time = time.time_ns()
    vp = fast_pow(c, d, p)
    vq = fast_pow(c, d, q)
    q_inv, p_inv = extgcd(q, p)
    xp = q * q_inv
    xq = p * p_inv
    m2 = (vp * xp + vq * xq) % n
    assert(m == m2) # make sure we get the correct plaintext
    print(f"{(time.time_ns() - start_time)} ns")

if __name__ == "__main__":
    main()