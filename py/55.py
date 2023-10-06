from num import *
    
maxiter = 50
lns = 0
for i in range(1, 10000):
    c = 0
    j = i + int(str(i)[::-1])
    while ispalin(j) != 1:
        j = j + int(str(j)[::-1])
        if c==maxiter:
            #print 'not found', i
            lns += 1
            break
        c += 1
print lns
