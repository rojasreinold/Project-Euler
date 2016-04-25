import math
def isPrime(num, array = [], *args):
    for i in range(0,len(array), +1):
        #print "%d" % array[i]
        if num % array[i] == 0:
            #print "divis by %d" % array[i]
            return False
        if math.sqrt(num) < array[i]:
            return True
    return True
listPrimes =[2]
currentNum = 3

while len(listPrimes) <1000000:
    if isPrime(currentNum, listPrimes):
        listPrimes.append(currentNum)
    currentNum += 2
    print "%d" % len(listPrimes)
    #print "length is: %d" % len(listPrimes)
#print "last one is : %d " % listPrimes[-1]

primeSum = 0

for i in range (0,len(listPrimes), +1):
    primeSum = primeSum + listPrimes[i]
    print "%d" % len(listPrimes)

print primeSum
