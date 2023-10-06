
import itertools

def replace69(l):
    for (i,item) in enumerate(l):
        if item in [6,9]: l[i] = -1
    return l
    
sqrs = []
for i in xrange(1,10):
    sqr = [(i*i)/10, (i*i)%10]
    sqrs.append(replace69(sqr))

combos = []
for c in itertools.combinations(xrange(10),6):
    combos.append(replace69(list(c)))

count = 0
for i in xrange(len(combos)-1):
    for j in xrange(i+1,len(combos)):
        good = True
        for sqr in sqrs:
            if not ((sqr[0] in combos[i] and sqr[1] in combos[j]) or \
            (sqr[0] in combos[j] and sqr[1] in combos[i])):
                good = False
                break
        if good: count += 1

print count
