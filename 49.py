import math
from num import *

p = {}
c = 0
for i in range(1000,9999):
    if isprime(i):
        c += 1
        k = str(''.join(sorted([x for x in str(i)])))
        if k in p:
            p[k].append(i)
        else: p[k] = [i]

for k,v in p.iteritems():
    if len(v) >= 3:
        for i in range(len(v)-2):
            for j in range(i+1,len(v)-1):
                 for k in range(j,len(v)):
                      if v[k]-v[j]==v[j]-v[i]: print v[i],v[j],v[k]

