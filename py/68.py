import time
import math
import itertools

st = time.time()
#print 'time:', time.time()-st

l = [x for x in range(1,11)]
#print 'l:',l
maxf = 0
maxl = []

def mn(a,b,c):
    return c+10*b+100*a

for p in itertools.permutations(l):
    c = p[0]+p[1]+p[2]
    if  p[3]+p[2]+p[4]==c \
    and p[5]+p[4]+p[6]==c \
    and p[7]+p[6]+p[8]==c \
    and p[9]+p[8]+p[1]==c:
        li = [mn(p[0],p[1],p[2]), mn(p[3],p[2],p[4]), mn(p[5],p[4],p[6]), \
              mn(p[7],p[6],p[8]), mn(p[9],p[8],p[1])]
        if min(li) > maxf:
            maxf = min(li)
            maxl = li
print ''.join([str(x) for x in maxl])
