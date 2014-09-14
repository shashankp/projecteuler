# fibo

cache = {}
cache[0] = 1
cache[1] = 2
def fib(n):
  if n not in cache:
     cache[n] = cache[n-1] + cache[n-2]
  return cache[n]

s = 0
n = 1
f = 2
while f < 4000000:
  if f%2==0:
    #print 'c'
    s += f
  n += 1
  f = fib(n)
  #print cache
  
print s
