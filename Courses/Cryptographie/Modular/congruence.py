def congru(a, mod):
    b = 0
    while (a-b)%mod != 0:
        b+=1
    
    return b

# It's a useless solution to describe congruence relation
# a ≡ b mod m meaning that a-b mod m = 0
# so we can write
# a ≡ b mod m <=> a % m = b

print(congru(11,6))
print(congru(8146798528947,17))

# equivalent of 
print(11%6)
print(8146798528947%17)
