#wording

w = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    '100':'hundred',
    1000:'one thousand',
}

def getwording(i):
    words = ''
    if i in w:
        words = w[i]
    else:
        if i < 100:
            w[i] = w[10*(i/10)] + ' ' + w[i%10]
            words = w[i]
        if i >= 100 and i < 1000:
            s = ''
            if i%100 > 0: s = ' and ' + w[i%100]
            w[i] = w[i/100] + ' ' + w['100'] + s
            words = w[i]
    return words

c = 0
for i in range(1,1001):
    c += len(getwording(i).replace(' ', ''))
print c
