import time

st = time.time()

infile = open('roman.txt','r')

val = {
'I': 1,
'V': 5,
'X': 10,
'L': 50,
'C': 100,
'D': 500,
'M': 1000
}

digitCount = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:2,
    5:1,
    6:2,
    7:3,
    8:4,
    9:2
    }

def charsSaved(r):
    v,n = 0,0
    prev,curr = 0,0
    for ri in r:
        curr = val[ri]
        if curr>prev:
            v += curr-2*prev
        else: v += curr
        prev = curr
    v1=v
    #print v%10, (v/10)%10, (v/100)%10, (v/1000)%10
    #if v>=1000:
    n = v/1000
    v %= 1000
    v2=v
    #print n,v
    while v!=0:
        n += digitCount[v%10]
        v /= 10
    #print r,v1,v2,n,len(r)-n
    return len(r)-n

totalSavings = 0
while True:
    l = infile.readline()
    if not l: break
    crudeRoman = l.strip()
    totalSavings += charsSaved(crudeRoman)
print totalSavings
#print 'time:', time.time()-st

'''
MMMMDCCCXCI


XXXXVIIII
XLIX
IL


XVI
XIIIIII
VVVI

XVIIII
XVIV
XIX

XXXXVIIII
XXXXIX
XLVIIII
LIX

XXXXX
L

MCCCCCCVI
MDCVI
'''
