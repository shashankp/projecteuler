def nextn(n):
    return sum([int(x)*int(x) for x in list(str(n))])

en = set([89])
maxi = 10000000
for i in range(1,maxi):
    #if i%500000==0: print i
    n = nextn(i)
    a = [i]
    while n != 1 and n not in en:
        a.append(n)
        n = nextn(n)
    if n != 1:
        for ai in a:
            en.add(ai)
print len([x for x in en if x < maxi])
