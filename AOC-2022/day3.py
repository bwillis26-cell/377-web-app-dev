file = open('day3-test.txt', 'r')
lines = file.readlines()

rucksack = "vJrwpWtwJgWrhcsFMMfFFhFp"

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

first_half = rucksack[:len(rucksack) // 2]
second_half = rucksack[len(rucksack) // 2:]
print(first_half)
print(second_half)

same_letter = None
score = 0
for letter in first_half:
    if letter in second_half:
        same_letter = letter
        print(alphabet.index(letter) + 1)
        break
print("Found common letter: " + same_letter)

for line in lines:
    line = line.strip()

    first_half = line[:len(line) // 2]
    second_half = line[len(line) // 2:]
    
    for letter in first_half:
        if letter in second_half:
            same_letter = letter
            score += alphabet.index(letter) + 1
            break
print("Part 1: " + str(score))

new_score = 0
rucksack = []
for line in lines:
    line = line.strip()
    if len(rucksack) == 3:
        print(rucksack)
        for letter in rucksack[0]:
            if letter in rucksack[1] and letter in rucksack[2]:
                new_score += alphabet.index(letter) + 1
                break

        rucksack =[]
    else:
        rucksack.append(line)

print("Part 2: " + str(new_score))


