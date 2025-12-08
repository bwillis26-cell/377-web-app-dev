file = open('day6-test.txt', 'r')
lines = file.readlines()

sum = 0
columns = []
lineList = []
for line in lines:
    line = line.strip()
    lineSplit = line.split(" ")
    for letter in lineSplit:
        if letter == "":
            lineSplit.remove(letter)
    lineList.append(lineSplit)
    print(lineList)





