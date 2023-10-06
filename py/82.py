infile = open('82.in','r')

n = 80
d = {}
for i in range(n):
    for j,v in \
     enumerate(map(int,\
     infile.readline().strip().split(','))):
     d[(i,j)] = v

for c in range(n-1)[::-1]:
    s = []
    for i in range(n): s.append(d[(i,c)])
    for r in range(n):
        l = []
        for ro in range(n):
            if ro==r: l.append(d[(ro,c)] + d[(ro,c+1)])
            else:
                v = d[(ro,c+1)] + sum(s[min(ro,r):max(ro,r)+1])
                l.append(v)
        d[(r,c)] = min(l)

ml = []        
for i in range(n):
    ml.append(d[(i,0)])
print min(ml)              
                
