#Helper functions

import sys, time, math, os

def ispalin(si): return str(si)==str(si)[::-1]
 
def getprimestill(maxm):
  ps = [2]
  for m in xrange(3,maxm,2):
      isprime = True
      for i in xrange(3,int(math.sqrt(m))+1):
          if m%i==0:
              isprime = False
              break
      if isprime: ps.append(m)
  return ps
 
def isprime(m):
  if m==2: return True
  if m<2 or m&1==0: return False
  for i in xrange(3,int(math.sqrt(m))+1):
    if m%i==0: return False
  return True
 
def gcd(a,b):
    while b>0: a,b = b,a%b
    return a
 
def lcm(a,b):
  return (a*b)/gcd(a,b)
 
def comb(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
 
#adding fractions #deprecated!
#a/b + c/d
def addfrac(p,q):
    x,y,z,w = p[0],p[1],q[0],q[1]
    d = lcm(y,w)
    n = x*d/y+z*d/w
    g = gcd(n,d)
    return ((n/g),(d/g))
 
if __name__ == '__main__':
  pass
