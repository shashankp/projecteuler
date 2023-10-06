import itertools

infile = open('59.in','r')
l = map(int, infile.readline().strip().split(','))
llen = len(l)

lrange = range(97,123)
validrange = range(32,123)

o = 0
for i in lrange:
    for j in lrange:
        for k in lrange:
            li = 0
            vs = 0
            for key in itertools.cycle([i,j,k]):
                if li==llen: break
                val = key^l[li]
                if val not in validrange: break
                li += 1
                vs += val
            if li == llen:
                #print 'found',i,j,k,vs
				o = vs
				break
print o
    
