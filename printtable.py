def printTable(input):
    ...


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colWidth = []




for i in tableData:
    max_width = 0
    for j in i:
        if len(j) > max_width:
            max_width = len(j)
    
    colWidth.append(max_width)

for i in range(4):
    for j in range(3):
        valu = tableData[j][i].rjust(colWidth[j])
        print(valu, sep="", end=" ")
    print()