'''
3 * d ≡ 1 mod 13
how to find d

have a look about the relation between 13 and 3

what are the prime numbers under 13, we can easily find them
so we have 1 3 5 7 11
As we can see 3 is coprime with 13
But 3 * d ≡ 1 mod 13 means that (3*d) mod 13 = 1
So we have to find a multiple of 3 such as (3*d)mod 13 = 1
here we are 3*9 = 27 = 13*2+1

In python it's exist the inverse function
'''

from Crypto.Util.number import inverse

print(inverse(3,13))