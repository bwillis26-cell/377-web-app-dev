file = open('p-13.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    line = int(line.strip())
    sum += line

print(sum)