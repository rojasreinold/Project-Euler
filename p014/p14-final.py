def collatzLength(num):
    #find the collatz length
    length = 0
    while num >1:
        if num%2 == 0:
            #Defined operation for even numbers
            length +=1
            num = num/2
        else:
            #Defined operation for odd numbers
            length += 1
            num = (3*num) +1
    return length+1

topLen = 0
currentLen = 0
value = 0
for i in range(2,1000000, +1):
    #check all collatz length for range, keep top length
    currentLen = collatzLength(i)
    if currentLen > topLen:
        print "prev was %d \t new is %d" % ( topLen, currentLen)
        topLen = currentLen
        value = i
print value 
