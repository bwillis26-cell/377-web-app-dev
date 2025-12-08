file = open('day7-test.txt', 'r')
lines = file.readlines()

counter = 0
array = []
for line in lines:
    line = line.strip()
    tempList = []
    for letter in line:
        tempList.append(letter)
    array.append(tempList)

print(array)
    
        
