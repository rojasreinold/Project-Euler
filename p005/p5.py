def isDiv(number):
    if (number % 17 > 0):
        return True
    if (number % 19 > 0):
        return True
    if (number % 16 > 0):
        return True
    if (number % 14 > 0):
        return True
    if (number % 13 > 0):
        return True
    if (number % 11 > 0):
        return True
    else:
        return False


num = 2520
while isDiv(2520):
    num = num + 2520
    print "%d" %num
print "%d" % num
