file = open('day2.txt', 'r')
lines = file.readlines()

score = 0  
for line in lines:
    line = line.strip()
    line = line.split(" ")
    if line[1] == "X":
        if line[0] == "A":
            score += 4
        elif line[0] == "B":
            score += 1
        else:
            score += 7
    elif line[1] == "Y":
        if line[0] == "A":
            score += 8
        elif line[0] == "B":
            score += 5
        else:
            score += 2
    else:
        if line[0] == "A":
            score += 3
        elif line[0] == "B":
            score += 9 
        else:
            score += 6
print(score)
    
    