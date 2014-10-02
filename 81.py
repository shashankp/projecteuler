infile = open('81.in','r')

n = 80
c = {}
for i in range(n):
    for j,v in \
     enumerate(map(int,\
     infile.readline().strip().split(','))):
     c[(i,j)] = v

for i in range(n)[::-1]:
    for j in range(n)[::-1]:
        l = []
        if j!=n-1: l.append(c[(i,j+1)]+c[(i,j)])
        if i!=n-1: l.append(c[(i+1,j)]+c[(i,j)])
        if l: c[(i,j)] = min(l)
        
print c[(0,0)]
