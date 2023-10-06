import time
import math
from num import *

st = time.time()

def enum(i):
    if i%3==0:
        return 2*i/3
    return 1

def revf(f):
    return (f[1],f[0])

def addf(f1,f2):
    den = f1[1]*f2[1]
    num = f1[0]*f2[1] + f1[1]*f2[0]
    g = gcd(num,den)
    return (num/g, den/g)

def eterm(i):
    j = i
    a = (enum(j),1)
    #print j, a, enum(j)
    while j != 0:
        a = addf((enum(j-1),1), revf(a))
        j -= 1
    return addf((1,1),revf(a))

n = eterm(100)[0]
numsum = sum([int(x) for x in str(n)])
print numsum
#print 'time:', time.time()-st
