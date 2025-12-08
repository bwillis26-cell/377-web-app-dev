file = open('day6-test.txt', 'r')
lines = file.readlines()

sum = 0
columns = []
for line in lines:
    line = line.strip()
    lineList = line.split(" ")
    print(lineList)


for i in range(len(lines[0])):
    if len(lines) == 5:
        columns.append([lines[0][i], lines[1][i], lines[2][i], lines[3][i], lines[4][i]])
    else:
        columns.append([lines[0][i], lines[1][i], lines[2][i], lines[3][i]])
print(columns)

