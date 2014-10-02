import sys

infile = open('54.in', 'r')

def convert(char):
    if char == 'A':
        return 1
    elif char == 'T':
        return 10
    elif char == 'J':
        return 11
    elif char == 'Q':
        return 12
    elif char == 'K':
        return 13
    else:
        return int(char)

def royal(counts):
    if counts[10] and counts[11] and counts[12] and counts[13] and counts[1]:
        return True
    else:
        return False

def straight(counts):
    for i in range(1, 10):
        for j in range(5):
            if counts[i+j]:
                if j == 4:
                    return True
                else:
                    continue
            else:
                break
    return False

def desc(l):
    c = []
    for i in range(len(l)):
        if l[i]==1: c.append(i)
    return sorted(c, reverse=True)


def hand(counts, ccounts, sameSuit):
    cp = counts[:]
    cp.append(cp.pop(1))
    #print 'c:',counts
    #print 'p:',cp
    
    if royal(counts) and sameSuit:
        return ['royal flush',10,[]]
    elif straight(counts) and sameSuit:
        return ['straight flush',9,[cp.index(1)]]
    elif ccounts[4] == 1:
        return ['four of a kind',8,[cp.index(4),cp.index(1)]]
    elif ccounts[3] == 1 and ccounts[2] == 1:
        return ['full house',7,[cp.index(3),cp.index(2)]]
    elif sameSuit:
        return ['flush',6,desc(cp)] #all cards in desc order
    elif straight(counts) or royal(counts):
        return ['straight',5,[cp.index(1)]]
    elif ccounts[3] == 1:
        return ['three of a kind',4,[cp.index(3),len(cp)-1-cp.index(1),cp.index(1)]]
    elif ccounts[2] == 2:
        return ['two pairs',3,[len(cp)-1-cp.index(2),cp.index(2),cp.index(1)]]
    elif ccounts[2] == 1:
        return ['pair',2,[cp.index(2)]+desc(cp)]
    else:
        return ['high card',1,desc(cp)]
    
win1 = 0
win2 = 0
tot = 0
while True:
    input = infile.readline().strip()
    if not input: break
    input = input.split(' ')
    #print input
    op1,op2 = [],[]
    for i in range(2):
        ccounts = [0]*5
        sameSuit = True
        counts = [0]*14
        result = ''

        counts[convert(input[0+5*i][0])] += 1
        for j in range(1+5*i, 5+5*i):
            if input[j-1][1] != input[j][1]:
                sameSuit = False

            counts[convert(input[j][0])] += 1
            ccounts[counts[convert(input[j][0])]] += 1
            ccounts[max(counts[convert(input[j][0])] - 1, 0)] -= 1

        if i==0:
            op1 = hand(counts, ccounts, sameSuit)
            #print '0:',counts
        else:
            op2 = hand(counts, ccounts, sameSuit)
            #print '0:',op1[0],op1[2]
            #print '1:',op2[0],op2[2]
            if op1[1] > op2[1]:
                win1 += 1
                #print 'good'
            elif op1[1]==op2[1]:
                for j in range(len(op1[2])):
                    if op1[2][j]>op2[2][j]:
                        win1+=1
                        #print 'good'
                        break
                    elif op1[2][j]<op2[2][j]: break
            tot += 1
print win1            #tot
