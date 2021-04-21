import timeit

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