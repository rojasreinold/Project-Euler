#Python3

#Using Combinations and permutations
multiple = 1
for i in range(1,41,+1):
    #finding total combinations factorial
    multiple *= i 
divide =1

#Finding the number of combiantions needed
for i in range(1,21,+1):
    divide *= i

for i in range(1,21,+1):
    divide *= i
print (multiple/divide)
