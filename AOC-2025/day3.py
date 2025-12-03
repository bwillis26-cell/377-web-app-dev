file = open('day3-test.txt', 'r')
lines = file.readlines()

total = 0

for line in lines:
    line = line.strip()
    num = ""
    numNums = 2
    index = -1
    

    for j in range(1, numNums + 1):
        max = 0
        for i in range(index + 1, len(line) - numNums + j):
            numNumNums = int(line[i])
            if numNumNums > max:
                max = numNumNums
                index = i
        num += str(max)
        
       

    total += int(num)

print(total)