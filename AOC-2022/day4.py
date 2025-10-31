file = open('day4.txt', 'r')
lines = file.readlines()


score = 0
for line in lines:
    line = line.strip()
    first, second = line.split(",")
    first = first.split("-")
    second = second.split("-")
    firstPart1 = int(first[0])
    firstPart2 = int(first[1])
    secondPart1 = int(second[0])
    secondPart2 = int(second[1])
    if (secondPart1 >= firstPart1) and (secondPart2 <= firstPart2):
        score += 1
    elif (firstPart1 >= secondPart1) and (firstPart2 <= secondPart2):
        score += 1

print(score)


score = 0
for line in lines:
    line = line.strip()
    first, second = line.split(",")
    first = first.split("-")
    second = second.split("-")
    firstPart1 = int(first[0])
    firstPart2 = int(first[1])
    secondPart1 = int(second[0])
    secondPart2 = int(second[1])
    if (firstPart1 <= secondPart2 and firstPart1 >= secondPart1) or (firstPart2 <= secondPart2 and firstPart2 >= secondPart1):
        score += 1
        print(line)
    elif (secondPart1 >= firstPart1) and (secondPart2 <= firstPart2) or (firstPart1 >= secondPart1) and (firstPart2 <= secondPart2):
        score += 1
        print(line)
print(score)