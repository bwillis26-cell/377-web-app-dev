file = open('day1.txt', 'r')
lines = file.readlines()

current = 0
max = 0
for line in lines:
    line = line.strip()
    if line == "":
        # Line is blank
        if current > max:
            max = current

            pass
        current = 0
    else:
        #Not a blank line, add 
        current += int(line)

print('Part 1: ' + str(max))


current = 0
maxes = [0, 0, 0]
for line in lines:
    line = line.strip()
    if line == "":
        if current > maxes[0]:
            maxes[0] = current
            maxes.sort()
        current = 0
    else:
        current += int(line)
print('Part 2: ' + str(sum(maxes)))
