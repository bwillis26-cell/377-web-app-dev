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


points.sort(key=lambda x: (x[0],0 if x[1] == "S" else 1))

active = 0
start = None
count = 0

i = 0
while i < len(points):
    pos = points[i][0]
    kind = points[i][1]

    if kind == "S":
        if active == 0:
            start = pos
        active += 1
    else:
        active -= 1
        if active == 0:
            end = pos
            count += end - start + 1
    i += 1

# Too High: 357485433193296
#           357485433193296
#           357485433193284
print(count)

    

    
             





