inp = [1, 10, 100, 1000, 10000, 100000, 1000000]
l = [9*i*10**(i-1) for i in range(1,7)]
s = []
for i in range(1, len(l)+1):
    s.append(reduce(lambda x,y:x+y, l[:i], 0))
print l, s

prod = 1
for i in inp:
    si = i
    j = 0
    while i > s[j]: j+=1
    if j>0: i-=s[j-1]
    #print i,'st digitof set', j+1
    k = int(str(10**j + (i-1)/(j+1))[(i-1)%(j+1)])
    #print 'digit#',i, k
    prod *= k
    
print prod
