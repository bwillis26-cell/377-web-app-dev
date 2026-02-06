import math

max = -1
start = 600851475143
startSqrt = int(math.sqrt(start) + 1)

while start % 2 == 0:
    max = 2
    start //= 2


for i in range(3, startSqrt, 2):
    while start % i == 0:
        max = i
        start // i
if start > 2:
    max = start


print(max)