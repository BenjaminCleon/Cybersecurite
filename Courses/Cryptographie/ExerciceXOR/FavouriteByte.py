# exercice inspired by https://cryptohack.org/courses/intro/xorkey0/

from operator import xor

val = bytes.fromhex('0073626960647f6b206821204f21254f7d694f7624662065622127234f726927756d').decode("utf-8")
for i in range(0, 2**8-1):
    res = ''.join(chr(xor(ord(value), i)) for value in val)
    if "crypto" in res:
        print(res)

# we should see crypto{0x10_15_my_f4v0ur173_by7e}