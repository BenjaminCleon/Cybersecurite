#algorythm to find one identy from Bezout


import math

def bezout(a, b):
    u = 1
    v = 0
    u1 = 0
    v1 = 1

    while b != 0:
        q = math.floor(a/b)
        r2 = a
        u2 = u
        v2 = v
        a = b
        u = u1
        v = v1
        b = r2-q*b
        u1 = u2-q*u1
        v1 = v2 - q*v1

    print(a, u, v)


bezout(26513, 32321)