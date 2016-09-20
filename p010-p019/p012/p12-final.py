import math
from time import clock
def listOfPrimes(size):
    #Finds a list of primes
    listPrimes = [2]
    currentNum = 3
    while  len(listPrimes)< size:
        i = 0
        while True:
            #if currentNum is divisible by a previous prime it is not prime
            if (currentNum %listPrimes[i] ==0) :
                break
            if math.sqrt(currentNum) <= listPrimes[i]:
                listPrimes.append(currentNum)
                break
            i += 1
        currentNum += 2
    return listPrimes

def DivByTotal(num, primes):
    #Find the total number of Divisors 
    totalDiv = 1
    i = 0
    divisors = []
    while True:
        if num % primes[i] ==0 :
            divisors.append(0)
            while num % primes[i] ==0:
                divisors[-1] += 1
                num = num/primes[i]
        elif num == 1 :
            for c in range(len(divisors)):
                totalDiv *= (divisors[c] +1)
            return totalDiv
        else:
            i += 1
startTime = clock()
triNumber = 1
i = 2
numDiv = 0
listPrimes = []
listPrimes = listOfPrimes(5000)

while numDiv < 500:
    #iterates over triangle Numbers
    triNumber += i
    numDiv = DivByTotal(triNumber, listPrimes)
    i += 1
print triNumber
print "Elapsed time was" , clock()-startTime
