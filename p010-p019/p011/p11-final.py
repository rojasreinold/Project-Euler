#Final version quickest version
import numpy as np
def largestDiagnalL2R(array, totalRows,totalCols):
    currentRowStart = 0 
    currentColStart = 0

    largestSum = 0
    currentSum = 0
    while currentRowStart < (totalRows-3):
        currentColStart = 0
        while currentColStart < (totalCols-3):
            currentCol = currentColStart
            currentRow = currentRowStart
            currentSum = 1
            i = 0
            while i <  4:
                currentSum *= array[currentRowStart + i][currentColStart + i]
                i += 1
            if currentSum > largestSum:
                largestSum = currentSum
            currentColStart += 1
        currentRowStart += 1
    return largestSum

def largestDiagnalR2L(array, rows, cols):
    currentRowStart = 0
    currentColStart = cols -1

    largestSum = 0
    currentSum = 0

    while currentRowStart < rows-3:
        currentColStart = cols-1
        while currentColStart >= 3:
            currentCol = currentColStart
            currentRow = currentRowStart
            currentSum = 1
            i = 0
            while i < 4:
                currentSum *=array[currentRowStart +i ][currentColStart -i]
                i +=1
            if currentSum > largestSum:
                largestSum = currentSum

            currentColStart -= 1
        currentRowStart += 1
    return largestSum

def largestDown(array,rows, cols):
    largestSum = 0
    currentSum = 0
    for i in range(cols):
        for c in range(rows-4):
            currentSum = 1
            for n in range(c,c+4):
                currentSum *= array[n][i]
            if currentSum > largestSum:
                largestSum = currentSum
    return largestSum

def largestLeft(array,rows, cols):
    #finds largest 4 group horizontally
    largestSum = 0
    currentSum = 0
    for i in range(rows):
        for c in range(cols-4):
            currentSum = 1
            for n in range(c, c+4):
                currentSum *= array[i][n]
            if currentSum > largestSum:
                largestSum = currentSum
    return largestSum

def printArray(array):
    #prints the 2dArray
    for i in range(size):
        for j in range(size):
            print '{:20}'.format(array[i][j]),
        print


with open('input.txt' ) as f:
    #open the file and add the lines into an array
    array = []
    for line in f:
        array.append(line)

#Following intializes some the arrays
size = 20
numArray = np.empty([size,size])
currentArray = [size]

for i in range(size):
    #Puts all of the lines into numArray
    currentArray = array[i].split()
    for n in range(size):
        numArray[i,n] = int(currentArray[n])

numDown = largestDown(numArray, size,size)
numLeft = largestLeft(numArray,size,size)
numDiagL2R = largestDiagnalL2R(numArray, size, size)
numDiagR2L = largestDiagnalR2L(numArray, size, size)

print "Larget Down  is\t\t %r" % numDown
print "largest left is\t\t %r" % numLeft
print "larget diagL2R is\t %r" % numDiagL2R
print "lragest diageR2L is\t %r" % numDiagR2L
