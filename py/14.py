# Collatz sequence

n = 1000000
mc = 0
mp = 0
for i in range(1,n+1):
    c = 1
    j = i
    #print 'i', i
    while i != 1:
        if i%2==0: i /= 2
        else: i = 3*i + 1
        c += 1
    if c > mc:
        mp = j
        mc = c
print mp
    
    
