import math

def listOfPrimes(size):
    listPrimes = [2]
    currentNum = 3
    while  len(listPrimes)< size:
        i = 0
        while True:
            if (currentNum %listPrimes[i] ==0) :
                break
            if math.sqrt(currentNum) <= listPrimes[i]:
                listPrimes.append(currentNum)
                break
            i += 1
        currentNum += 2
    print " found list of primes"
    return listPrimes

def DivByTotal(num, primes):
    output = open("output.txt", 'w')
    totalDiv = 0
    i = 0
    divisors = []
    while True:
        output.write("i is %d \n" % i)
        output.write( "num is %d\n" % num)
        output.write( "primes[i] is %d\n" % primes[i])
        if num % primes[i] ==0 :
            #output.write( " i is %d" % i)
            #output.write("num was %d" % num)
            #output.write( "prime was %d" % primes[i])
            num = num/primes[i]
            #print "after division num was %d" %num
            divisors.append(primes[i])
        elif num == 1 :
            return totalDiv
        else:
            i += 1

triNumber = 1
i = 2
numDiv = 0
listPrimes = []
listPrimes = listOfPrimes(500)

triNumDoc = open("triNums.txt", 'w')
while numDiv < 500:
    triNumber += i
    numDiv = DivByTotal(triNumber, listPrimes)
    triNumDoc.write("TriNum is %d \t\tdivby: %d\n" % (triNumber, numDiv))
    i += 1
