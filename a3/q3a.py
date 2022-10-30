e = 65537 # public key (given)
m = 466921883457309 # (given)

p = 173829016889224829217511816865562808154359946203329147631898008878979005249574957229416952857653653417335041840825132834799458846735474572227701120428842212670204990377679952495476841529793128620104820871662994760397907533400114286949880530440124465041291503379749072421970518598984228421203914763044529866424
q = 51111283233075774196700253541324535904203359626244723652980811716872006078330230425498621061903657712662690078425201484007369157686231281279757959815525759774791407549712737741876311442866124193059151905792934429565374261504441935808599869834711128039714370791377121022845947408736064563701802244583680490384
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
        y -= x * (a / b)
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
    # TODO:
    # 0. get the private key
    # d, _ = extgcd(e, euler_totient(n)) # private key
    
    # 1. encrypt m to c
    c = fast_pow(m, e, n)

    # 2. decrypt c with CRT, profile it
    # 3. decrypt c without CRT, profile it

if __name__ == "__main__":
    main()