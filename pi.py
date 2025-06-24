import math 

pi = float(0.0)
positive = True

for term in range (1,100000000,2):
    factor = 4/term
    if ( positive ):
        pi += factor
    else:
        pi -= factor

    positive = not positive

print(pi)
print(math.pi)