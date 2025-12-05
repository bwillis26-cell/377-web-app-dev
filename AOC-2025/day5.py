file = open('day5.txt', 'r')
lines = file.readlines()

ranges = []
nums = []
points = []
spaceCheck = 1
for line in lines:
    line = line.strip()
    if line == "":
        spaceCheck = 2
    elif spaceCheck % 2 == 1:
        rangeOne, rangeTwo = [int(x) for x in line.split("-")]
        points.append([rangeOne, "S"])
        points.append([rangeTwo, "E"])
        ranges.append((rangeOne, rangeTwo))
    else:
        nums.append(line)


points.sort(key=lambda x: (x[0],0 if x[1] == "s" else 1))

sum = 0
start = points[0][0]
sCounter = 0
for i in range(len(points)):
    firstVal = points[i][0]
    secondVal = points[i][1]
    if secondVal == "S":
        sCounter += 1
    elif secondVal == "E":
        sCounter -= 1
        end = firstVal
    if sCounter == 0:
        num = end - start + 1
        sum += num
        if i < len(points) - 1:
            start = points[i + 1][0]


# Too High: 357485433193296
print(ranges)
print(sum)

    

    
             





