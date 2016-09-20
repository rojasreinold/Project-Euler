def isPrime(factor):
    divisible = factor /2
    while divisible > 1:
        if factor % divisible == 0:
            return False
    return False



def isAFactor(number, factor):
    if number % factor == 0:
        return True
    else:
        return False

def findLargestPrime(number):
    factor = number/2

    while factor > 1:
        if isAFactor(number, factor):
            print "about to check for a prime"
            if (isPrime(factor)):
                return factor

        factor = factor - 2
        print "Factor is now %d" % factor
    return 1


number = 600851475143

factor = findLargestPrime(number)
print "The largest prime of %d is %d" % (number, factor)
