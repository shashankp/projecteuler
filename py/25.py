#fibo
 
cache = {}
cache[0] = 1
cache[1] = 2
def fib(n):
  if n not in cache:
     cache[n] = fib(n-1) + fib(n-2)
  return cache[n]

n = 10**1000
i = 2
f = fib(i)
while f < n:
  i += 1
  f = fib(i)
  
print i-2
