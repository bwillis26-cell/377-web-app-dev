file = open('day2.txt', 'r')
line = file.readlines()[0].strip(",")

invalidID = []

sum = 0

ids = line.split(",")

for id in ids:
    start, end = (int(x) for x in id.split("-"))
    for i in range(start, end + 1):
        quags = str(i)
        length = len(quags)
        for j in range(1, length):
            if length % j == 0:
                chunks = [quags[k:k + j] for k in range(0, len(quags), j)]
                if len(set(chunks)) == 1:
                    sum += i
                    break
        
            

    
print(sum)