import math
import time

'''
nCk
prob = k*(k-1)/(n*(n-1)) = 1/2
=> 2k**2 + 2*k - n**2 - n = 0

solve above Diophantine Eq:
solutions for k,n is a recurrence relation :
k1 = 3*k0 + 2*b0 -2
n1 = 4*k0 + 3*b0 -3
'''

st = time.time()
am = 10**12
a,b = 15,21
while True:
	a,b = 3*a+2*b-2, 4*a+3*b-3
	#print a,b
	if b>am: 
		print a
		exit()
			
#print 'time:', time.time()-st
