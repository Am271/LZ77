def LCSubStr(X, Y, m, n):

	LCSS = [[0 for k in range(n+1)] for l in range(m+1)]


	result = 0
	length = 0
	common = []

	if(X[0] in Y):
		for i in range(m + 1):
			for j in range(n + 1):
				if (i == 0 or j == 0):
					LCSS[i][j] = 0
				elif (X[i-1] == Y[j-1]):
					LCSS[i][j] = LCSS[i-1][j-1] + 1
					result = max(result, LCSS[i][j])
				else:
					LCSS[i][j] = 0
		
		for i in range(n + 1):
			if LCSS[1][i] ==  1 and not length:
				length = 1
				common.append(Y[i-1])
				continue
			if length :
				try:
					if LCSS[length+1][i]:
						length += 1
						common.append(Y[i-1])
				except:
					pass
		if Y[len(Y)-length] == X[length]:
			length += LCSubStr(Y[len(Y)-length:len(Y)],X[length:len(X)],len(Y[len(Y)-length:len(Y)]),len(X[length:len(X)]))
			
	return length


# Driver Code
X = 'rarrad'     #lab
Y = 'adabrar'   #sb

X1 = [i for i in X]
Y1 = [j for j in Y]
# X = 'ofghxx'    lab
# Y = 'xxxxoof'   sb



m = len(X1)
n = len(Y1)

print('Length of Longest Common Substring is',
	LCSubStr(X1, Y1, m, n))