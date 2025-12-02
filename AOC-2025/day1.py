file = open('day1.txt', 'r')
lines = file.readlines()

dial = 50
count1 = 0
count2 = 0
for line in lines:
    line = line.strip()
    
    amount = int(line[1:])

    direction = line[0]

    for i in range(amount):
        if direction == "L":
            dial = (dial - 1 + 100) % 100
        else:
            dial = (dial + 1) % 100
        if dial == 0:
            count2 += 1
    if dial == 0:
        count1 += 1
    
    
    
    
    
print(count2)



