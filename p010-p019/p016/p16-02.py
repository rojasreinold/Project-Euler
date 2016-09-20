carrot = 1

for i in range(0,1000, +1):
    carrot *= 2

carrotSum = 0

carrotString = str(carrot)
for i in range(len(carrotString)):
    carrotSum += int(carrotString[i])

print (carrotSum)
