#in python3
def findSum():
    with open('input.txt', 'r') as f:
        #add all numbers to an array
        array = []
        for line in f:
            array.append(int(line))
    numSum = 0
    for i in range(len(array)):
        numSum += array[i]
    print (numSum)
findSum()
