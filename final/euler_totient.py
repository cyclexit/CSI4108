def euler_totient(n):
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
    n = int(input("n = "))
    print(f"ϕ({n}) = {euler_totient(n)}")

if __name__ == "__main__":
    main()
