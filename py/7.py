# prime : 1001st
from num import isprime
 
n = 10001
 
i = 2
c = 2
while i <= n:
  while True:
    c += 1
    if isprime(c):
       #print 'prime#',i,c
       break
  i += 1
print c
