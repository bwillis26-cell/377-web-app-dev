file = open('day5.txt', 'r')
lines = file.readlines()

stacks = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]
mainStacks = [['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
              ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
              ['F', 'B', 'H', 'W', 'P', 'M', 'Q'],
              ['V', 'S', 'T', 'D', 'F'],
              ['Q', 'L', 'D',' W', 'V', 'F', 'Z'],
              ['Z', 'C', 'L', 'S'],
              ['Z', 'B', 'M', 'V', 'D', 'F'],
              ['T', 'J', 'B'],
              ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H'] ]


for line in lines:
    line = line.strip()
    splitList = line.split(" ")
    numBlocks = int(splitList[1])
    numFrom = int(splitList[3]) - 1
    numTo = int(splitList[5]) - 1

    for i in range(numBlocks):


        block = mainStacks[numFrom].pop()
        mainStacks[numTo].append(block)

for i in range(len(mainStacks)):
    print(mainStacks[i][-1], end='')