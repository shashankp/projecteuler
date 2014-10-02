import sys
import time
import math
import itertools

st = time.time()

def getlist(val):
    l = []
    n = 1
    t = val(n)
    while t < 10**4:
        if t >= 10**3 and t%100>=10: l.append(t)
        n += 1
        t = val(n)
    return l

def flist(a,l):
    t = 100*(a%100)
    return [x for x in l if x>t and x<t+100]

sqs = getlist(lambda x: x*x)
trs = getlist(lambda x: (x*(x+1))/2)
pens = getlist(lambda x: (x*(3*x-1))/2)
hexs = getlist(lambda x: (x*(2*x-1)))
heps = getlist(lambda x: (x*(5*x-3))/2)
octs = getlist(lambda x: (x*(3*x-2)))
al = [sqs, trs, pens, hexs, heps]

pl = [x for x in range(5)]
for o in octs:
    for p in itertools.permutations(pl):
        for li0 in flist(o,al[p[0]]):
            for li1 in flist(li0,al[p[1]]):
                for li2 in flist(li1,al[p[2]]):
                    for li3 in flist(li2,al[p[3]]):
                        li4 = 100*(li3%100)+(o/100)
                        if li4 in al[p[4]]:
                            a=[o,li0,li1,li2,li3,li4]
                            print sum(a)
                            #print 'time:', time.time()-st
                            sys.exit()
