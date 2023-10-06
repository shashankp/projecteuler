import num
import time
import itertools
import exceptions
import operator

class Frac():
    def __init__(self,pn,pd):
        self.n, self.d = pn, pd
    def __add__(self,x):
        nn,nd = self.n*x.d + self.d*x.n, self.d*x.d
        gc = num.gcd(nn,nd)
        return Frac(nn/gc,nd/gc)
    def __sub__(self,x):
        nn,nd = self.n*x.d - self.d*x.n, self.d*x.d
        gc = num.gcd(abs(nn),abs(nd))
        return Frac(nn/gc,nd/gc)
    def __mul__(self,x):
        nn,nd = self.n*x.n, self.d*x.d
        gc = num.gcd(abs(nn),abs(nd))
        return Frac(nn/gc,nd/gc)
    def __div__(self,x):
        if x.n==0: raise 'divby0'
        nn,nd = self.n*x.d, self.d*x.n
        gc = num.gcd(abs(nn),abs(nd))        
        return Frac(nn/gc,nd/gc)
    def pr(self):
        print str(self.n)+'/'+str(self.d)

start = time.time()
m,maxst,ml = 0, set([]), []
funs = [ lambda x,y,z,l: x(l[0],y(z(l[1],l[2]),l[3])),
         lambda x,y,z,l: x(l[0],y(l[1],z(l[2],l[3]))),
         lambda x,y,z,l: z((x(l[0],y(l[1],l[2]))),l[3]),
         lambda x,y,z,l: z(y(x(l[0],l[1]),l[2]),l[3]),
         lambda x,y,z,l: y(x(l[0],l[1]),z(l[2],l[3]))
       ]

o = [operator.add, operator.sub, operator.div, operator.mul]
s = range(1,10)
for p in itertools.combinations(s,4):
    pl = [Frac(x,1) for x in p]
    st = set()
    for x in o:
        for y in o:
            for z in o:
                for l in itertools.permutations(pl,4):
                    for f in funs:
                        try:
                            nn = f(x,y,z,l)
                            if nn.d==1 and nn.n>0: st.add(nn.n)
                        except:
                            pass #print 'bad'
    for i in xrange(1,100):
        if i not in st:
            if  i>m+1:
                m = i-1
                #print m
                maxst,ml = st,pl
            break

for w in ml: print w.n,
#print '\n',m, maxst,time.time() - start,'s'
