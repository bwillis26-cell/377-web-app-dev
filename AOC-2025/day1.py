file = open('day1-test.txt', 'r')
lines = file.readlines()

dial = 50
count = 0
for line in lines:
    line = line.strip()
    
    if len(line) == 2:
        amount = int(line[1])
    elif len(line) == 3:
        amount = int(line[1:3])
    else:
        amount = int(line[1:4])

    direction = line[0]

    if direction == "L":
        dial -= amount
        
    else:
        dial += amount
        
    
    print(dial)
    
    dial = dial % 100
    print(dial)
    dial = abs(dial)
    print("     ")

    count += (amount // 100)
    
    
    
    
print(count)



