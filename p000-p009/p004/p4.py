def isAPal(number):
    sNumber = str(number)
    length = len(sNumber)
    #following checks if is a palinoramous number
    for i in range(0,length,+1):
        if (not(sNumber[i] == sNumber[length -1 -i])):
            return False
    return True

def largestPal(basePal):
    num1= 999
    num2 = 999
    while basePal<=num1*999:
        num2 =999
        while (num1*num2> basePal):
            if (isAPal(num1*num2)):
                #if number is a pal proceed to next index(just for speed)
                basePal = num1*num2
                break
            num2 -= 1
        num1 -= 1
    return basePal

def onePal():
    #Find a Pal to serve as the base pal
    for num1 in range(999,99,-1):
        for num2 in range(999,99,-1):
            if isAPal(num1*num2):
                return num1*num2



firstPal = onePal()
truePal = largestPal(firstPal)
print "The largest pal is %d" % truePal
