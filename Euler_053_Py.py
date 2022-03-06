#Ariel Tynan
#Euler Problem 053, Combinatoric selections, solved in Python
#Started and finished 5 March 2022

import math
count = 0
for n in range(1,101):
    for r in range(1,n):
        if math.factorial(n)/(math.factorial(r)*math.factorial(n - r)) > 1000000:
            count = count + 1
print(count)
