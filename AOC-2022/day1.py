file = open('day1.txt', 'r')
lines = file.readlines()

current = 0
max_list = [0, 0, 0]
for line in lines:
    line = line.strip()
    if line == "":
        # Line is blank
        if current > max_list[0]:

          

        
    else:
        #Not a blank line, add 
        current += int(line)

print('Part 1: ' + str(max))
