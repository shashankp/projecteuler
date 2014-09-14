#45228

def factors(n):
    l = []
    for i in range(1,1+n/2):
        if n%i==0: l.append(i)
    return l

def digitslist(i):
    return list(str(i))

def dupes(i):
    return len(list(str(i))) != len(set(str(i)))

total = 0
for i in range(1000, 10000):
    if not dupes(i):
        for f in factors(i):
            if dupes(f) or dupes(i/f): continue
            s = digitslist(i)+digitslist(f)+digitslist(i/f)
            if len(s) == len(set(s)) and '0' not in s and len(s) == 9:
                #print 'found', i, f, i/f
                total += i
                break
print total        
