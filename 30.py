#max digits : 6

c = dict([str(i),i**5] for i in range(10))
print c

s = 0
for i in range(11,10**6):
    sc = sum([c[x] for x in str(i)])
    if i==sc:
        #print i, sc
        s += i
print s        
