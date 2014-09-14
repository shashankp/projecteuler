#spiral
n = 1001
c = 1

if n % 2 == 1:
  for i in range(3,n+1,2):
    #topright, topleft, downleft, downright
    s = i*i + (i*i - i + 1) + ((i-1)**2 + 1) + ((i-1)**2 - i + 2)
    c += s
    #print i, 's:', s, 'c:', c

print c
    
