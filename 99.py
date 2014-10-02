import time
import math
import copy

st = time.time()

infile = open('99.in','r')

l = []
i = 1
maxv = 0.0
maxi = 0
while True:
    il = infile.readline()
    if not il: break
    j = map(int, il.strip().split(','))
    v = j[1]*math.log(j[0])
    if v > maxv:
        maxv = v
        maxi = i
        #print v, i
    i += 1
print maxi

