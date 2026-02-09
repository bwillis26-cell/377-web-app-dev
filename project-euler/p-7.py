import math

def isPrime(num):
    for i in range(2, round(math.sqrt(num))):
        if num % i == 0:
            return False
        
    return True

count = 1
i = 3

while count <= 10001:
    if isPrime(i):
        count += 1

    i += 2

print(i)