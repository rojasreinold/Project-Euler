def findSum():

    with open('input.txt') as f:
        nums = f.read()
    nums = map(int,nums)
    numSum = sum(nums)
    return numSum


data = findSum()
print data
