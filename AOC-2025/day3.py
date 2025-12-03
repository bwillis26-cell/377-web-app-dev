file = open('day3.txt', 'r')
lines = file.readlines()

total = 0



max1 = 0
max1Index = 0
max2 = 0
max2Index = 0
for line in lines:
    line = line.strip()
    max1 = line[0]
    max2 = line[1]
    tempList = []
    tempString = ""
    for i in range(2, len(line)):
        if max2 > max1:
            max1 = max2
            max2 = line[i]        
        elif line[i] > max2:
            if max2 > max1:
              max1 = max2
              max2 = line[i]
            else:
                max2 = line[i]
            
    tempList.append(max1)
    tempList.append(max2)
    tempString = tempList[0] + tempList[1]
    
    total += int(tempString)
            

print(total)