def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


print(gcd(10, 5))     # → 5
print(gcd(48, 18))    # → 6
print(gcd(100, 75))   # → 25
print(gcd(17, 13))    # → 1

