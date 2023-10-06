infile = open('83.in','r')

def neighbors(i,j):
    l = []
    if i>0 : l.append((i-1,j))
    if i<n-1 : l.append((i+1,j))
    if j>0: l.append((i,j-1))
    if j<n-1: l.append((i,j+1))
    return l
    
n = 80
d = {}
a = {}
for i in range(n):
    for j,v in \
     enumerate(map(int,\
     infile.readline().strip().split(','))):
     d[(i,j)] = v
     a[(i,j)] = -1

a[(0,0)] = d[(0,0)] #starting point

while True:
    prev = a[(n-1,n-1)]
    for (i,j) in [(p,q) for p in range(n) for q in range(n)]:
        if i==0 and j==0: continue
        val = [a[k] for k in neighbors(i,j) if a[k]!=-1]
        a[(i,j)] = min(val) + d[(i,j)]
    if a[(n-1,n-1)] == prev: break #stable final cost
    #else: print 'do it again...'
            
print a[(n-1,n-1)]
