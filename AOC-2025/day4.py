file = open('day4-test.txt', 'r')
lines = file.readlines()

def count_neighbors(y, x):
    atCount = 0
    if y == lengthGrid - 1:
        if x != 0 and x != lengthRow - 1:
            if grid[y][x - 1] != ".":
                atCount += 1
            if grid[y][x + 1] != ".":
                atCount += 1
            if grid[y - 1][x] != ".":
                atCount += 1
            if grid[y - 1][x - 1] != ".":
                atCount += 1
            if grid[y - 1][x + 1] != ".":
                atCount += 1
    elif y == 0:
        if x != 0 and x != lengthRow - 1:
            if grid[y][x - 1] != ".":
                atCount += 1
            if grid[y][x + 1] != ".":
                atCount += 1
            if grid[y + 1][x] != ".":
                atCount += 1
            if grid[y + 1][x - 1] != ".":
                atCount += 1
            if grid[y + 1][x + 1] != ".":
                atCount += 1
    else:
        if x == 0:
            if grid[y][x + 1] != ".":
                atCount += 1
            if grid[y - 1][x + 1] != ".":
                atCount += 1
            if grid[y + 1][x] != ".":
                atCount += 1
            if grid[y - 1][x] != ".":
                atCount += 1
            if grid[y + 1][x + 1] != ".":
                atCount += 1
        elif x == lengthRow - 1:
            if grid[y][x - 1] != ".":
                atCount += 1
            if grid[y - 1][x - 1] != ".":
                atCount += 1
            if grid[y + 1][x] != ".":
                atCount += 1
            if grid[y - 1][x] != ".":
                atCount += 1
            if grid[y + 1][x - 1] != ".":
                atCount += 1
        else:
            if grid[y - 1][x] != ".":
                atCount += 1
            if grid[y - 1][x + 1] != ".":
                atCount += 1
            if grid[y - 1][x - 1] != ".":
                atCount += 1
            if grid[y][x - 1] != ".":
                atCount += 1
            if grid[y][x + 1] != ".":
                atCount += 1
            if grid[y + 1][x - 1] != ".":
                atCount += 1
            if grid[y + 1][x] != ".":
                atCount += 1
            if grid[y + 1][x + 1] != ".":
                atCount += 1

    return atCount

grid = []

for line in lines:
    row = [x for x in line.strip()]
    grid.append(row)

totalAt = 0
lengthGrid = len(grid)
lengthRow = len(grid[0])

while True:
    
    for y in range(lengthGrid):
        for x in range(lengthRow): 
            if grid[y][x] == "@":    
                if count_neighbors(y, x) < 4:
                    totalAt += 1
                    grid[y][x] = "X"

    if totalAt == 0:
        break
    totalAt = 0

    for j in range(lengthGrid):
        for i in range(lengthRow):
            if grid[j][i] == "X":
                grid[j][i] == "."

    
    
print(totalAt)
totalP2 = 0

for k in range(lengthGrid):
    print(grid[k])
    for l in range(lengthRow):
        if grid[k][l] == "@":
            totalP2 += 1

print(totalP2)
            





# for row in grid:
#     print("".join(row))

