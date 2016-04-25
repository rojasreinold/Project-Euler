def getDivisible(num, divBy):
    addTo = num
    while (num % divBy > 0):
        num+= addTo
    return num

num = 2520
divBy = 11
while (divBy <20):
    num = getDivisible(num, divBy)
    print "%d" % num
    divBy += 1
print "%d" %num
