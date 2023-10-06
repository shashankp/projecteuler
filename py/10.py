#sum of primes
import math
from num import *

n = 2000000
s = 2
for i in xrange(3, n):
  if isprime(i): s += i
print s
