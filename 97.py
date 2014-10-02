#28433*2**(7830457)+1
import math
import time

st = time.time()
n = 1
for i in range(1,7830457+1):
    n = (n*2)%10**10
#print n,1+n*28433    
print str(1+n*28433)[-10:]
#print 'time: ', time.time()-st
