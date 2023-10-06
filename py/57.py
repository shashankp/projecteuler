from num import *

c = {1:(3,2)}
s = 0
for i in range(2,1001):
    f = addfrac((1,1),c[i-1])
    n = addfrac((1,1),(f[1],f[0]))
    c[i] = n
    if len(str(n[0])) > len(str(n[1])):
        s += 1
print s
