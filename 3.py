# primes
import math
from num import *

n = 600851475143
maxf = 0
for i in xrange(3, int(math.sqrt(n)) + 1, 2):
  if n%i==0 and isprime(i):
    maxf = i
print maxf
