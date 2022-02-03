# we will use the XOR process between two datas with differents types
# XOR consist to take each bit of a data and do the next operation
# if bits are the same we return 0 else we return 1

def xor(ba1, ba2):
    return ba1^ba2
    
res = ''.join(chr(xor(ord(value), 13)) for value in "label" )

print(res)

# second option
# res = ''
# for value in "label":
#     res += chr(xor(ord(value), 13)) # with from operator import xor

# print(res)