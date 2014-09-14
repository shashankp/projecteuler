# curious no; factorial
# 7 digits limit
import math

o = 0
for i in range(3, 99999):
    s = 0
    for j in [math.factorial(int(x)) for x in list(str(i))]:
        if s > i: break
        s += j
    if i == s :
        #print i
        o+=i
print o        
