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

while currentNum < 2000000:
    i=0
    while True:
        if  (currentNum % listPrimes[i] == 0) :
            break
        
        if math.sqrt(currentNum) <= listPrimes[i]:
            listPrimes.append(currentNum)
            break
        i += 1
    currentNum += 2
    #print " %d" % len(listPrimes)
primeSum = 0

for i in range (0,len(listPrimes), +1):
    primeSum = primeSum + listPrimes[i]

print primeSum
