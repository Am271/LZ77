def compare(X, Y, m, n):

	LCSS = [[0 for k in range(n+1)] for l in range(m+1)]

	length = 0
	common = []
	offset = 0

	if(X[0] in Y):
		for i in range(m + 1):
			for j in range(n + 1):
				if (i == 0 or j == 0):
					LCSS[i][j] = 0
				elif (X[i-1] == Y[j-1]):
					LCSS[i][j] = LCSS[i-1][j-1] + 1
				else:
					LCSS[i][j] = 0
		# print(LCSS)
		for i in range(n + 1):
			if LCSS[1][i] ==  1 and not length:
				length = 1
				common.append(Y[i-1])
				offset = len(Y) - i + 1
				continue
			if length:
				try:
					if LCSS[length+1][i] and LCSS[length][i-1]:
						length += 1
						common.append(Y[i-1])
				except:
					pass
			
		# print(length)
		tY = Y[len(Y) - offset:len(Y) - offset + length]
		tX = X[length:]
		if tY[0] == X[length]:
			dummy, tlength = compare(tX, tY, len(tX), len(tY))
			length += tlength
			
	return offset, length


# Driver Code
# X = 'rarrad'     #lab
# Y = 'adabrar'   #sb

# X = 'ofghxx'	#lab
# Y = 'xxxoxxf'	#sb

X = 'rarrax'
Y = 'xwdxrar'

# X = 'bbcxdf'
# Y = 'asfbbac'

X1 = [i for i in X]
Y1 = [j for j in Y]

m = len(X1)
n = len(Y1)

print('Length of Longest Common Substring is',
	compare(X1, Y1, m, n))