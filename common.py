def common(l1,l2):#takes lab and sb and returns offset and the number of common characters
	common = []
	offset = 0

	if(l2[0] in l1):# find lcs only if 1st char in l2 exists in l1
		for i in range(len(l2)):
			for j in range(len(l1)):
				if(len(common)==0):
					if(l1[j] == l2[i]):
						common.append(l1[j])
						offset = len(l1)-j
						break;
				elif(len(common)>0 and (j>0 and l1[j-1] == l2[i-1]) and l1[j] == l2[i]):
					common.append(l1[j])


	print("".join(common))

	print(offset)
	return offset,len(common)


#str1 = 'abcdaf'
#str2 = 'bcdf'
str1 = 'bfcbab'
str2 = 'bfcr'
l1 = list(str1)
l2 = list(str2)
common(l1,l2)
# print(common(l1,l2))