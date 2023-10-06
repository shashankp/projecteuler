#lcm
 
n = 20
def lcm(a,b):
  c = a*b
  while b>0:
    a,b = b,a%b
  return c/a
 
l = set()
for i in xrange(2, n):
  if i%2 != 0: l.add(2*i)
  else: l.add(i)
 
c = 1
for i in l:
  c = lcm(c,i)
print c
