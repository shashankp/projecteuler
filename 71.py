import time
import math
from num import *

st = time.time()

def gr(x,y):
    if x[0]*y[1]-y[0]*x[1] > 0: return True
    return False

def bw(a,b,c,d,den):
    num = (c*den)//d
    if gr((num,den),(a,b)) and gr((c,d),(num,den)):
        return num
    return n-1

l = (0,1)
for d in range(10**6,1,-1):
    n =  bw(0,1,3,7,d)
    if n > 0:
        nf = (n,d)
        if gr(nf,l):
            l = nf
            #print n,'/',d
print l[0]        
#print 'time:', time.time()-st
