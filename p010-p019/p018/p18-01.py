class Pyramid:
    __init__(self, firstBlock):
        top = Row(firstBlock)
        bottom = top
        rows = 1
    
    def addRow(self):
        rows += 1
        

class Row:
    blocks = []
    __init__(self, r):
        blocks.append(r)
    def nextRow(self, r):
        nextRow = r
         


with open("input.txt") as f:
    array = []
    for line in f:
        array.append(line)
    

for i in range(len(array)):
    

