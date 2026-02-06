max = 0
maxCheck = True
start = 600851475143


for i in range(1, start):
    if start % i == 0:
        for j in range(1, i):
            if i % j == 0:
                maxCheck = False

    if maxCheck:
        max = i


print(max)