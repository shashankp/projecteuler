#palindrome
 
def ispalin(si): return str(si)==str(si)[::-1]
 
aux=0
for k in range(101,1000):
    for j in range(101,1000):
            if ispalin(str(j*k)) and j*k>aux:
                    aux=j*k
print aux
