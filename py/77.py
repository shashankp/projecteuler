import time
from num import *

st = time.time()
c = {}

#no of ways of summing to n, with all elems <= m
def go(n,m):
    if (n,m) in c: return c[(n,m)]
    s = 0
    pm = [x for x in p if x<=m]
    for i in pm:
        if n-i==0: s += 1
        elif n>i: s += go(n-i,i)
    c[(n,m)] = s
    return s

n = 71
t = 0
p = getprimestill(n)
#print p
for i in p:
    s = go(n-i,i)
    #print i,s
    t += s
#print 'total:', t
if t>5000: print n
#print 'time:', time.time()-st
