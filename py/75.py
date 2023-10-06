import time
import math
from num import gcd

st = time.time()

l = 1500000    
d = [0]*l
o = int(math.sqrt(l))
for i in range(1,o,2):
    for j in range(2,o,2):
        if gcd(i,j)==1:
            s = abs(i*i-j*j) + 2*i*j + i*i + j*j
            for k in range(s, l, s):
                d[k] += 1
                
print d.count(1)
#print 'time:', time.time()-st
