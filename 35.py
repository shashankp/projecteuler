# primes
import math
import itertools
from num import *

n = 1000000
l = ['1','3','7','9']
o = set(['2','5'])

def iscircularprime(s):
  primes = []
  for j in range(len(s)):
    i = int(''.join(s[j:] + s[:j]))
    if not isprime(i): return []
    primes.append(i)
  return primes

for i in range(1, len(str(n-1)) + 1):
  c = list(itertools.product(l, repeat=i))
  for p in c:
    for q in iscircularprime(list(p)):
      o.add(q)
      
print len(o)
     
