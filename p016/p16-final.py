#Python3

carrot = 1

#Find 2^1000
for i in range(0,1000, +1):
    carrot *= 2

carrotSum = 0

carrotString = str(carrot)
#add all the values of each character inthe string
for i in range(len(carrotString)):
    carrotSum += int(carrotString[i])

print (carrotSum)
