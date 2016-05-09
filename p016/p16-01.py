carrot = 1

for i in range(0,1000, +1):
    carrot *= 2

print (carrot)
carrotSum = 0
while carrot > 0:
    current = carrot%10
    carrotSum += current
    carrot -= current
    carrot = carrot/10
print (carrotSum)
