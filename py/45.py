#Triangular, pentagonal, and hexagonal

import math

def isperfsq(i):
    sq = math.sqrt(i)
    if sq == int(sq): return True
    return False

n = 533
c = 0
while True:
    h = n*(2*n-1)
    if isperfsq(8*h+1) and isperfsq(24*h+1):
        t = (-1+math.sqrt(8*h+1))
        p = (1+math.sqrt(24*h+1))
        if t%2!=0 or p%6!=0:
            n += 1
            continue
        t /= 2
        p /= 6
        #print 'found', h
        if (p*(3*p-1))/2 == (t*(t+1))/2:
             #print 't', t, (t*(t+1))/2
             #print 'p', p, (p*(3*p-1))/2
			 print int((t*(t+1))/2)
			 exit()
    n += 1
