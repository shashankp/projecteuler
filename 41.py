import math
import itertools
from num import *

m = 2143
l = [str(x) for x in range(1,10)]
o = 0
for i in range(3,len(l)+1):
  for p in itertools.permutations(l[:i]):
    n = int(''.join(p))
    if isprime(n) and n>m:
		#print 'found', n
		o = n
		m = n
print o
