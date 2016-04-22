def sumOfSquares(num):
    sums= 0
    for i in range(1, num+1, +1):
        sums = sums + (i*i)
    return sums

def squareOfSum(num):
    sums = 0
    for i in range(1, num+1, +1):
        sums = sums + i 
    squares = sums*sums
    return squares

num =100

difference = squareOfSum(num) - sumOfSquares(num)
print "%d" % difference
