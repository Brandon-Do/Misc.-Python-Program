def gcd(a, b):
    if a == b:
        return a
    if b == 0 or a == 0:
        return a + b
    if a > b:
        return gcd(b, a % b)
    return gcd(a, b % a)

print(gcd(1200, 612))