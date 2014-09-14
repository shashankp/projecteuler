# recurring decimal part

n = 1000
mp = 0
mv = 1
for i in range(2, n):
    rs = [0] #remainders
    r = 10**(1+i/10)
    c = 0
    while r%i not in rs:
        rs.append(r%i)
        r = 10*(r%i)
        c += 1
    p = len(rs[rs.index(r%i):])
    if p > mp:
        #print i, ':', p
        mp = p
        mv = i
print mv
