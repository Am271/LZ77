def LCSubStr(X, Y, m, n):
	#initializing all elements with a default value of zero 
	LCSS = [[0 for k in range(n+1)] for l in range(m+1)]

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

# Driver Code
# X = 'rarrad'     #lab
# Y = 'adabrar'   #sb

X = 'opoppp' #lookahead buffer
Y = 'xxoppyu' #search buffer

# X = 'bbcrcc' #lab
# Y = 'bfcbbac'  	#sb

# X = 'raxdar' #lab
# Y = 'daqxraq' #sb

# X = 'raxdar' #lab
# Y = 'darxrag' #sb

# X = 'ofghxx'    #lab
# Y = 'xxxoofg'   #sb

# X = 'abmzx' #lab
# Y = 'qabxmz' #sb

# X = 'raxdar' #lab
# Y = 'daraxag' #sb

# X = 'ofghxx'  #lab
# Y = 'xxxoxxf' #sb
 
X1 = [i for i in X]
Y1 = [j for j in Y]


m = len(X1) # number of rows
n = len(Y1) #number of columns

print('Length of Longest Common Substring is',
	LCSubStr(X1, Y1, m, n))