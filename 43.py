import itertools

l = [str(x) for x in range(10)]
s = 0
for p in itertools.permutations(l):
    sv = ''.join(p)
    if sv[5]=='0' or sv[5]=='5':
        if int(sv[3])%2==0:
            if int(sv[2:5])%3==0: #sum([int(x) for x in sv[2:4]])
                if int(sv[4:7])%7==0:
                    if int(sv[5:8])%11==0:
                        if int(sv[6:9])%13==0:
                            if int(sv[7:10])%17==0:
                                #print sv
                                s += int(sv)
print s                                
