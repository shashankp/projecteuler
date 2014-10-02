import math
from num import *

st = time.time()

maxi = 10**4
p = [2]
for i in range(3,maxi,2):
    if isprime(i): p.append(i)

def nprimefac(i):
  return len([x for x in p if x<i/2 and i%x==0])

i = 2*3*5*7
while i<10**6:
  #print i
  if i in p: i+=1
  elif i+3 in p or nprimefac(i+3)!=4: i+=3
  elif nprimefac(i)==4 and nprimefac(i+1)==4 and nprimefac(i+2)==4:
        print i
        break
  else : i += 1
      
#print 'time:', time.time()-st
#if i not in p and nprimefac(i)==4 and nprimefac(i+1)==4 and nprimefac(i+2)==4 and nprimefac(i+3)==4:
