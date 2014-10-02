#use cont fraction
import time
import math
from num import *

def rev(p): return (p[1],p[0])

def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if math.sqrt(n)==int(math.sqrt(n)):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

#print CF_of_sqrt(2)

def conv(l,i):
    i -= 1
    n = l[0]
    n, l = l[0], l[1:]
    lx = lambda j: l[j%len(l)]
    f = (lx(i),1)
    while i>0:
        f = addfrac((lx(i-1),1), rev(f))
        i -=1
    return addfrac((n,1),rev(f))
    
sq = []    
for i in range(1,34):
    sq.append(i*i)

xmax = 0
dmax = 0
for d in range(2,1001):
    if d in sq: continue
    l = CF_of_sqrt(d)
    k = 1
    while True:
        '''
        Look for fundamental solutions in h/k in all fractions in cont-fractions of d
        '''
        (x,y) = conv(l,k)
        if x*x-d*y*y==1:
            if x > xmax:
                xmax = x
                dmax = d
            break
        k += 1
print dmax#, xmax
