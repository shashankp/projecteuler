#preprocess: each name in newline & sort

infile = open('22.in', 'r')
i = 0
score = 0
while True:
    l = infile.readline().strip()
    if not l: break
    i += 1
    c = 0
    for j in l:
        c += ord(j)-ord('A')+1
    score += c*i
    #if i == 938: print l, i, c
print score
