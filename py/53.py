#print 'nCr > 1000000'

m = 1000000
n = 100
c = 0
for i in range(23,n+1):
    p = i
    j = i
    while p < m and i > 1:
        i -= 1
        p = (p*i)/(j-i+1)
    if p > m:
        #print j, j-i+1, p
        c += len(range(j-i+1,i))
print c
