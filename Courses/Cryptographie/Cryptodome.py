# When we use cryptosystems such as AES or RSA, we need to do operatical operation however a message is usually made up character
# So we convert our message into numbers
# to do that we can do like this
# if my message is WELL_PLAYED
# we use the ascii value
# convert them into hexa numbers
# concatenate hexa values
# transform into base 10 value
# to do that you can for convert into deciaml value use the function int.from_bytes if you have python 3.2 or more
# else you can use bytes_to_long from the api Cryptodrome
# to revert use long_to_bytes from the api Cryptodrome

from Crypto.Util.number import *

print(int.from_bytes(b'Well played', 'big'))
print(long_to_bytes(int.from_bytes(b'Well played', 'big')))