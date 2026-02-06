import math

max = 0
start = 600851475143
startSqrt =(int) (math.sqrt(start) + 1)


for i in range(3, startSqrt, 2):
    while start % i == 0:
        max = i
        start // i
if start > 2:
    max = start


print(max)