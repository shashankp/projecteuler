
'''

assuming 1 - horizontal step & 0 - vertical step
arranging 20 1''s and 20 0''s in 40 slots
40!/(20! * 20!) = 137846528820

'''


n = 20
r = {}
r[(0,0)] = 0
for i in range(1,n+1):
    r[(0,i)] = 1
    r[(i,0)] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        r[(i,j)] = r[(i-1,j)]+r[(i,j-1)]

print r[(20,20)]
