def isPrime(num, array = [], *args):
    for i in range(0,len(array), +1):
        #print "%d" % array[i]
        if num % array[i] == 0:
            #print "divis by %d" % array[i]
            return False
    return True
listPrimes =[2]
currentNum = 3
while len(listPrimes) <10001:
    if isPrime(currentNum, listPrimes):
        listPrimes.append(currentNum)
    currentNum += 2
    print "length is: %d" % len(listPrimes)
print "last one is : %d " % listPrimes[-1]
