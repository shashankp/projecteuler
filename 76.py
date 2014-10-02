import time
import math

st = time.time()
c = {}

#no of ways of summing to n, with all elems <= m
def go(n,m):
    if (n,m) in c: return c[(n,m)]
    if n==1: return 1
    s = 0
    for i in range(1,m+1):
        if n-i==0: s += 1
        elif n>i: s += go(n-i,min(n-i,i))
    c[(n,m)] = s
    return s

n = 100
t = 0
for i in range(1,n):
    s = go(i,min(i,n-i))
    #print i,s
    t += s
print t
#print 'total:', t   
#print 'time:', time.time()-st
