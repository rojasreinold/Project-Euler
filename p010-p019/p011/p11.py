import numpy as np
def largestDiagnal(array):
    pass

def largestUp(array):
    pass

def largestDown(array):
    pass

def largestLeft(array):
    pass

def largestRight(array):
    pass

array = np.zeros((20,20))

def readMatrixFile(f):
    data = []
    rows, cols = map(int,f.readline().split())
    for i in range(0, rows):
        data.append(map(float,f.readline().split()[:cols]))
    a = np.array(data)
    return a

def printMatrix(a):
    print " Matirix["+ ("%d" %a.shape[0]) + "][" +("%d" % a.shape[1]) + "]"
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0,cols):
        for i in range(0,cols):
            print "%7g" %a[i,j],
        print
    print

f = open("input.txt")
a = readMatrixFile(f)
printMatrix(a)
