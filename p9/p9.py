import math

def cIsInteger(a,b):
    c= (a*a) + (b*b)
    c = math.sqrt(c)
    if c.is_integer():
        return True
    else:
        return False
def checkFormula(a ,b):
    first = a*2000
    second = b*2000
    third = a*b
    sumIs = (1000**2) -first - second + third
    print "a: %d \t b: %d " % (a, b)
    if sumIs == 0:
        return True
    return False

def getPy():
    while True:
        for a in range(1,1000, +1):
            for b in range(1,1000,+1):
                if checkFormula(a,b):
                    if cIsInteger(a,b):
                        return (a ,b)
a, b= getPy()
print "a is %d and b is %d" % (a,b)
