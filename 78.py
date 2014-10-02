#prob78
#55374

#p(k) = p(k - 1) + p(k - 2) - p(k - 5) - p(k - 7) + p(k - 12) + p(k - 15) - p(k - 22) 
 
pentagonal = lambda x: (x*(3*x-1))/2

k,p = [],[1]

#generalized_pentagonal
for i in xrange(1,500):
    k.append(pentagonal(i))
    k.append(k[-1] + i)

i,val = 0,1
while True:
    i += 1
    val = 0
    for j in xrange(len(k)):        
        if k[j]>i: 
            break
        else: 
            val += (-1 if j%4>1 else 1)*(p[i-k[j]])
    p.append(val)
    val %= 10**6
    if val==0: break
        
print i
