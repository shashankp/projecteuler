import time
import math

st = time.time()

def CF_of_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.mcs.surrey.ac.uk/Personal/R.Knott/Fibonacci/cfINTRO.html
        In the section named: "Methods of finding continued
        fractions for square roots"
    """
    if math.sqrt(n)==int(math.sqrt(n)):
        return [int(math.sqrt(n))]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((math.floor(math.sqrt(n)) + step1_num) / step1_denom)
        ans.append(int(nextn))

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
            ans.append(ans[0] * 2)
            break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

#print CF_of_sqrt(2)

s = 0
for d in range(2,10001):
    if (len(CF_of_sqrt(d))-1)%2==1: s+=1
print s    
        
