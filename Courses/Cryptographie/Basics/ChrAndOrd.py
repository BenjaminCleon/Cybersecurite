# array which contains value in ASCII value
code = [87, 101, 108, 108, 32, 112, 108, 97, 121, 101, 100]

# join return a string with a separator such as '' or ' ' (whatever you want), with values containing in code array
# chr convert an ascii value to a string such as 65 equals 'A'
# number is the current number in code so here we go through the loop
res = ''.join(chr(number) for number in code)
print(res)

# as you guess ord do the invert of chr, moreover we use str to convert int into string for deny errors
print(' '.join(str(ord(letter)) for letter in res))
