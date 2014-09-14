#triangle sum

infile = open('18.in', 'r')

c = []
l = ''
while True:
    l = infile.readline()
    if len(l) == 0: break
    c.append(map(int, l.strip().split(' ')))

d = [[] for _ in range(len(c))]
d[len(d)-1] = c[len(c)-1]

for i in range(len(c)-2,-1,-1):
     for j in range(len(c[i])):
         d[i].append(c[i][j] + max(d[i+1][j], d[i+1][j+1]))
print d[0][0]

        
    


