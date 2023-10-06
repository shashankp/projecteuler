# max product diag

c = {}
n = 20
f = open('11.in', 'r')
def ReadData(foo):
    return list(map(foo, f.readline().strip().split(' ')))

def cache(i,j):
    return int(c[(i,j)])

for i in range(n):
   line = ReadData(str)
   for j in range(len(line)):
       c[(i,j)] = line[j]

#print c
m = 0
for i in range(n-3):
    for j in range(n-3):
        #print cache(i,j) , cache(i+1,j) , cache(i+2,j) , cache(i+3,j)
        vp = cache(i,j) * cache(i+1,j) * cache(i+2,j) * cache(i+3,j)
        hp = cache(i,j) * cache(i,j+1) * cache(i,j+2) * cache(i,j+3)
        dp1 = cache(i,j) * cache(i+1,j+1) * cache(i+2,j+2) * cache(i+3,j+3)
        dp2 = cache(i+3,j) * cache(i+2,j+1) * cache(i+1,j+2) * cache(i,j+3)
        m = max(max(hp, vp), max(max(dp1, dp2), m))
print m        
        
