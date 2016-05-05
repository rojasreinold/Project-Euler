def findSum():
    with open('input.txt', 'r') as f:
        array = []
        for line in f:
            array.append(int(line))
            #print ("did a line \n")
    numSum = 0
    for i in range(len(array)):
        numSum += array[i]
        #print ("added one from array \n")
    print (numSum)
findSum()
