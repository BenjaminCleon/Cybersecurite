# quadratic residue means that the equation 
# pow(x,2) is congruent to a(mod p) is solvable
# here is an exemple with p = 29 and the value 16,6,11 as pow(x,2)

for val in [14,6,11]:
    for a in range(29):
        if pow(a,2,29) == val:
            print(val, a)

# we find as quadratic residue the number 6 and their differents square root are 6 and 21 