import math

def isPrime(num):
    if num == 2 or num == 3:
        return True

    if num % 2 == 0:
        return False
    
    if num < 2:
        return False
    

    for i in range(3, round(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
        
    return True


max = 2000001
sum = 0
for i in range(1, max):
    if isPrime(i):
        sum += i


print(sum)