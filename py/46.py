from num import *

n = 10**4
sq = []
p = []
for i in range(n):
    if isprime(i): p.append(i)
    sq.append(2*i*i)

for i in range(1,n,2):
    if i in p: continue
    found = False
    for j in range(1,i):
        if i-sq[j] in p:
            found = True
            break
    if not found and i!=1:
		print i
		exit()
