'''
first digit of x is 1
since if > 1: no of digits of 6*x = digits of x + 1
'''

i = 142850
while True:
    if str(i)[0] == '1':
        l = sorted(list(str(i)))
        if l == sorted(list(str(2*i))) and l == sorted(list(str(3*i))) \
                and l == sorted(list(str(4*i))) and l == sorted(list(str(5*i))) \
                and l == sorted(list(str(6*i))):
            print i#,2*i,3*i,4*i,5*i,6*i,l
            break
    i += 1
        
        
