# algorythm to find gcd between two numbers

def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(a, b)

    return gcd(b, a%b)

print(gcd(800, 24))
