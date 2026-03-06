import random
file = open('diceware.txt', 'r')
lines = file.readlines()
words = []
wordDice = []
for i in range(5):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    d5 = random.randint(1, 6)
    wordDice.append(str(d1) + str(d2) + str(d3) + str(d4) + str(d5))
for line in lines:
    line = line.strip()
    line = line.split()
    for i in range(5):
        if line[0] == wordDice[i]:
            words.append(line[1])
print(" ".join(words))