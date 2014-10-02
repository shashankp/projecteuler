import time
import math
from num import *

st = time.time()

c = 0
for d in range(3,12001):
    for n in range(d/3,1+d/2):
        if gcd(n,d)==1 and d>2*n and d<3*n: 
            c += 1#print n,d
print c    
#print 'time:', time.time()-st
