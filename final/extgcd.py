# Solve the Diophantine equation a * x + b * y = c
# a, b and c are given, and x and y are unknowns
# The equation is solvable if c = gcd(a, b)
def extgcd(a: int, b: int):
    if b == 0:
        return (1, 0)
    else:
        y, x = extgcd(b, a % b)
        y -= x * (a // b)
        return (x, y)

def main():
    a = int(input("a = "))
    b = int(input("b = "))
    x, y = extgcd(a, b)
    print(f"({a}) * ({x}) + ({b}) * ({y}) = {a * x + b * y}")

if __name__ == "__main__":
    main()
