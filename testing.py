def slide(buf, ch):
    #buf is the buffer that will be slided, ch is the character that will be added at the last position after sliding
    for i in range(len(buf)-1):
        buf[i] = buf[i + 1]
    buf[len(buf) - 1] = ch

# search buffer = xxxxoof character added is b
teststr = 'xxxxoof'
testbuf = [i for i in teststr]
# print('{} takes {} usec/loop'.format(slide.__name__, timeit.timeit(slide(testbuf, 'b'), number=1000)*1000))

print(testbuf) #before sliding
slide(testbuf, 'b') #sliding, b is the character that will be added to the last position
print(testbuf) #after sliding

def compare(sbuf, labuf, j):
    if labuf[0] in sbuf and j > -1 and j < len(sbuf):
        offsets = []; matches = []; tmp = []; ttmp = []
        flag = 0
        for i in range(len(labuf)):
            while j > -1 and j < len(sbuf):
                if sbuf[j] == labuf[i]:
                    offsets.append(len(sbuf) - j)
                    tmp.append(sbuf[j])
                    flag = 1
                    j += 1; break
                else:
                    j -= 1
        if len(tmp) > 0:
            ttmp = compare(sbuf, labuf, len(sbuf) - max(offsets) - 1)
        if len(ttmp) > 0:
            return ttmp
        else:
            return tmp
    else:
        return []

sbuf = [i for i in 'xofgxof']
labuf = [i for i in 'ofghxx']

print(compare(sbuf, labuf, len(sbuf) - 1))