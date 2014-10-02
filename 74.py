import time
import math
global c,r

st = time.time()
def sumfact(i):
     if i in c: return c[i]
     sf = sum([math.factorial(int(x)) for x in str(i)])
     c[i] = sf
     return sf

c = {}
cnt = 0
for i in range(10**6):
    n=i
    l=[n]
    while len(l)<61:
        n = sumfact(n)
        if sumfact(n)==n: break
        if n in l:
            if len(l)==60: cnt += 1
            break
        l.append(n)
print cnt#,'time: ', time.time()-st        
        
    

        
