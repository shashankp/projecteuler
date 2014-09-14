from num import *

def dectobin(n):
    b = ""
    while n > 0:
        b = str(n%2) + b
        n /= 2
    return b

s = 0
for i in range(10**6):
    if ispalin(i) and ispalin(dectobin(i)):
        s += i
print s        
