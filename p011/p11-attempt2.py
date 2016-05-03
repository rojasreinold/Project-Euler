import numpy as np
def largestDiagnalL2R(array, rows, cols):
    pass

def largestDiagnalR2L(array, rows, cols):
    pass

def largestDown(array,rows, cols):
    largestSum = 0
    currentSum = 0
    for i in range(cols):
        for c in range(rows-4):
            currentSum = 1
            for n in range(c,c+4):
                currentSum *= currentSum[n][i]
                if currentSum > largestSum:
                    largestSum = currentSum
    pass

def largestLeft(array,rows, cols):
    pass

def printArray(array):
    #print the array. Used for debugging
    for i in range(size):
        for j in range(size):
            print '{:20}'.format(array[i][j]),
        print


with open('input.txt' ) as f:
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

for i in range(size):
    for j in range(size):
        print '{:20}'.format(numArray[i][j]),
    print
