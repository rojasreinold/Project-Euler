sumMul= 0
i=1
while i < 1000:
	if (i %3 ==0):
	#if i is divisible by 3 add it to the sumMul
		sumMul += i
	elif (i %5 == 0 ):
	#if i is divisible by 3 but the previous if statement was false add to sumM
		sumMul+= i
	
	i += 1
print"The sum will be %d" % sumMul
#this will print the valeu of sumMul
