#pythagorean triplet
  
d = {}
p = 450
for c in range (1, p):
  for b in range(1, p):
    for a in range(1,p):
     if a*a + b*b == c*c :
       #print 'found', c, b, a
       if a+b+c not in d: d[a+b+c] = [1,set([a,b,c])]
       elif d[a+b+c][1] != set([a,b,c]): d[a+b+c][0] += 1

m = 0
mn = 0
for k,v in d.items():
  if v[0] > m:
    mn = k
    m = v[0]
print mn     
