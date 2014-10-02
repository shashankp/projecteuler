from num import *

'''
limits of primes for powers
2: 7071
3: 370
4: 84
'''

lim = 50000000

def pows(e):
    pw = []
    for i in p:
        s = int(math.pow(i,e))
        if s < lim: pw.append(s)
        else: break
    return pw


p = getprimestill(int(math.sqrt(lim)))
sq = pows(2)
cb = pows(3)
qd = pows(4)

l = set([])
for q in qd:
    for c in cb:
        for s in sq:
            l.add(s+c+q)
l = [x for x in l if x < lim]
print len(l)
