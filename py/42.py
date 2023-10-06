infile = open('42.in', 'r')

sums = []
s = 0
i = 1
while s < 365: #max word len: 14, maxval:14*26
    s = (i*(i+1))/2
    sums.append(s)
    i += 1
#print len(sums), sums

c = 0
while True:
    l = infile.readline().strip()
    if not l: break
    s = 0
    for i in l:
        s += ord(i) - ord('A') + 1
    if s in sums: c += 1
        
print c
