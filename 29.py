'''
a**b == c**d
=> a**b = a**(e*d)
b = e**d
e [2,6]
e**d <= 100

e,d
2,[2,50]
3,[2,33]
4,[2,25]
5,[2,20]
6,[2,16]
=> 134
99*99 - 134
'''

#make list of all powers
p = set([])
for i in range(2,101):
    for j in range(2,101):
        p.add(j**i)

print len(p)
