import math
import time

st = time.time()
global r

def isgood(x):
    if x<0: return False
    q = math.sqrt(24*x+1)
    if q == int(q) and (q+1)%6==0:
        r = (q+1)/6
        return True
    return False

p = [((i*(3*i-1))/2) for i in range(10**4)]

for i in range(1,10000):
    for j in range(i+1,10000):
        l = abs(p[i]-p[j])
        if isgood(l) :
            k = p[i]+p[j]
            if isgood(k): 
				print l
				exit()
        
