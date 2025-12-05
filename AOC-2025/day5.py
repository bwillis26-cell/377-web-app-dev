file = open('day5.txt', 'r')
lines = file.readlines()

ranges = []
nums = []
spaceCheck = 1
for line in lines:
    line = line.strip()
    if line == "":
        spaceCheck = 2
    elif spaceCheck % 2 == 1:
        ranges.append(line)
    else:
        nums.append(line)
sum = 0
for i in range(len(nums)):
    num = int(nums[i])
    for j in range(len(ranges)):

        rangeOne, rangeTwo = [int(x) for x in ranges[j].split("-")]

        if num >= rangeOne and num <= rangeTwo:
            sum += 1
            break

print(sum)


