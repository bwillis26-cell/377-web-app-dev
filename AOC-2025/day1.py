file = open('day1-test.txt', 'r')
lines = file.readlines()

dial = 50
count = 0
for line in lines:
    line = line.strip()
    if line.length() == 2:
        amount = line[1]
    else:
        amount = line[1, 3]

    direction = line[0]
    # if direction == "L":
    print(amount)

