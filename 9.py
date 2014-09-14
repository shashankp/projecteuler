#pythagorean triplet
import itertools
  
for c in range (334, 999):
  for b in range(333, 1000-c):
     a = 1000 - c - b
     if a*a + b*b == c*c :
       print a*b*c
       break
     
