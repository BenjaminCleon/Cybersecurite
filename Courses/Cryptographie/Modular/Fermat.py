'''
Looking at Fermat's little theorem

we can resume things like this

if n is prime then pow(a,n-1) ≡ 1 mod n and pow(a,n) ≡ a mod n

So lets check
        pow(273246787654, 65536) mod 65537
Notice that 65536 is exactly 65537-1,
If 273246787654 and 65537 are coprime,
        then the result is one
'''

from math import gcd


if ( gcd(273246787654,65537) == 1 ):
    print(1)
