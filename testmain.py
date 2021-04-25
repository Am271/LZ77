import random
class olc:
    def __init__(self, o, l, c):
        self.offset = o
        self.length = l
        self.character = c

def slide(buf, ch):
    #buf is the buffer that will be slided, ch is the character that will be added at the last position after sliding
    for i in range(len(buf)-1):
        buf[i] = buf[i + 1]
    buf[len(buf) - 1] = ch

def genStr(sst, leN):
    stg = [random.choice(sst) for i in range(leN)]
    return ''.join(stg)

def LCSubStr(X, Y, m, n):
	#initializing all elements with a default value of zero 
	LCSS = [[0 for k in range(n+1)] for l in range(m+1)]

	offset = 0
	result = 0
	note_down = 0 #Holds the row number at which the lenght of LCS THAT OCCURS FIRST is found

	if(X[0] in Y):
		for i in range(m + 1):
			for j in range(n + 1):
				if (i == 0 or j == 0):
					LCSS[i][j] = 0
				elif (X[i-1] == Y[j-1] and i == 1):
					LCSS[i][j] = LCSS[i-1][j-1] + 1
					result = max(result, LCSS[i][j])
					note_down = i
				elif (X[i-1] == Y[j-1] and LCSS[i-1][j-1] == i-1):#increment only when the previous diagonal element value 
					LCSS[i][j] = LCSS[i-1][j-1] + 1				  #matches the previous row number (i-1) which inturn was 
					result = max(result, LCSS[i][j])			  #incremented from a row value sub to the 2nd row
					note_down = i     							  #Note that 1st row is always zero
				else:
					LCSS[i][j] = 0
		m=max(LCSS[note_down])
		offset = n-LCSS[note_down].index(m) + result	 #n = size of sb, n-index of max + result(which is the lenght of LCSS)

		# temporary Y refers to the new sb in recursion case
		# tY = X[:result] #it can alternatively be tY = Y[len(Y)-offset:len(Y)-offset+result]
		# temporary X refers to the new lab in recursion case
		tX = X[result:]
		tY = Y[len(Y)-offset:]
		# recursion condition 
		if tY[0] == X[result] and result == len(tY):#true only when the first element of lab is repeated at length of LCSS(result) index position
			dummy, tlength = LCSubStr(tX, tY, len(tX), len(tY)) #dummy holds the offset that is later discarded
			result += tlength									#since we do not need the new offset of value in recursion case
	return offset,result

def decode(L, declist):
    global sbufsize
    flag = ['x' for i in L if not i.offset < sbufsize + 1 and i.length < sbufsize + 1]
    decstr = ""
    if not flag:
        for values in L:
            if not values.offset and not values.length:
                declist.append(values.character)
            elif values.length > values.offset:
                nl = declist[len(declist)-values.offset:]
                declist.extend(nl)
                decode([olc(values.offset, values.length-values.offset, values.character)], declist)
            else:
                nl = declist[len(declist)-values.offset:len(declist)-(values.offset-values.length)]
                declist.extend(nl)
                declist.append(values.character)
        decstr = "".join(declist)
    return decstr

def readFile():
    f = open('data.txt')
    data = f.readlines()
    newstr = ' '.join(data)
    newstr = newstr.split('\n')
    data = ''.join(newstr)
    f.close()
    return data

# strin = menu()
# labufsize, sbufsize = getsize()
labufsize, sbufsize = 500, 600
strin = readFile()

sbuf = ['_' for i in range(sbufsize)]; labuf = []; o = 0; l = 0; olclist = []; k = labufsize

for i in range(labufsize):
	labuf.append(strin[i])

while True:
	o, l = LCSubStr(labuf, sbuf, len(labuf), len(sbuf))
	olclist.append(olc(o, l, labuf[l]))
	if labuf[1] == '_':
		break
	for j in range(l + 1):
		slide(sbuf, labuf[0])
		if k < len(strin):
			slide(labuf, strin[k])
			k += 1
		else:
			slide(labuf, '_')
for i in olclist:
	print(vars(i))

print('Encoding done!')
strout = decode(olclist, [])
# print('Input string: ' + strin + '\nOutput string: ' + strout)
print('Decoding done!')
if strout[-1] == '_':
	strin = strin + '_'
if strin == strout:
	inte = 'OK'
else:
	inte = 'Failed'
print(inte)
# print(strout == strin)