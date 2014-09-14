#748317
import math
from num import *

def truncs(n):
    l = []
    sn = str(n)
    for i in range(1,len(sn)):
        l.append(int(sn[:i]))
        l.append(int(sn[i:]))
    return l

c = 0
n = 11
total = 0
primes = [2,3,5,7]

while c < 11:
    if isprime(n):
        primes.append(n)
        if all(m in primes for m in truncs(n)):
            #print 'found', n
            c += 1
            total += n
    n += 1
print total    
