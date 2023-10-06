#ispalin

def ispalin(s):
    return str(s)==str(s)[::-1]

max=0
for i in xrange(999,99,-1):
    a,b,c = i/100, (i/10)%10, i%10
    n = 1000*i + 100*c + 10*b + a
    #print i,n
    for j in xrange(101, 1000):
        if n%j==0 and n/j<999:
            print n
            break
    if j!=999: break

