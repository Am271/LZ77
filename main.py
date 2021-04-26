import random
class olc:
    def __init__(self, o, l, c):
        self.offset = o
        self.length = l
        self.character = c

def slide(buf, ch):
    for i in range(len(buf)-1):
        buf[i] = buf[i + 1]
    buf[len(buf) - 1] = ch

def genStr(sst, leN):
    stg = [random.choice(sst) for i in range(leN)]
    return ''.join(stg)

def LCSubStr(X, Y, m, n):
	LCSS = [[0 for k in range(n+1)] for l in range(m+1)]

	offset = 0
	result = 0
	note_down = 0

	if(X[0] in Y):
		for i in range(m + 1):
			for j in range(n + 1):
				if (i == 0 or j == 0):
					LCSS[i][j] = 0
				elif (X[i-1] == Y[j-1] and i == 1):
					LCSS[i][j] = LCSS[i-1][j-1] + 1
					result = max(result, LCSS[i][j])
					note_down = i
				elif (X[i-1] == Y[j-1] and LCSS[i-1][j-1] == i-1):
					LCSS[i][j] = LCSS[i-1][j-1] + 1
					result = max(result, LCSS[i][j])
					note_down = i
				else:
					LCSS[i][j] = 0
		m=max(LCSS[note_down])
		offset = n-LCSS[note_down].index(m) + result

		tX = X[result:]
		tY = Y[len(Y)-offset:]
		if tY[0] == X[result] and result == len(tY):
			dummy, tlength = LCSubStr(tX, tY, len(tX), len(tY))
			result += tlength
	return offset,result

def encode(strin, sbuf, labuf, sbufsize, labufsize):
	o = 0; l = 0; olclist = []; k = labufsize
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
	return olclist

def print_encoding(olclist):
	for i in olclist:
		print(vars(i))

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

def menu():
	choice = input('1. Generate a random string\n2. Enter a string\n> ')
	# choice = '1'
	if choice == '2':
		strinp = input('String: ')
	elif choice == '1':
		base = input('Source characters: ')
		strinp = genStr(base, 16)
	else:
		print('Try again')
		exit()
	return strinp

def getsize():
	print('Look-ahead buffer size: 6\nSearch buffer size: 7')
	choice = input('1. Let it remain the same\n2. Change buffers\' size\n> ' )
	if choice == '1':
		a = 6; b = 7
	else:
		a = int(input('New search buffer size: '))
		b = int(input('New look-ahead buffer size: '))
		print('Size changed!')
	return a, b

strin = menu()
labufsize, sbufsize = getsize()
sbuf = ['_' for i in range(sbufsize)]; labuf = []

olclist = encode(strin, sbuf, labuf, sbuf, labufsize)
print_encoding(olclist)

strout = decode(olclist, [])
strout = strout.strip('_')
print('Input string: ' + strin + '\nOutput string: ' + strout)
