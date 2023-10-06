m = 0
i = 100
s = 0
for a in range(1,i):
    for b in range(1,i):
        s = sum([int(x) for x in list(str(a**b))])
        if s > m:
            m = s
            #print a,b,s
			
print m	

            
