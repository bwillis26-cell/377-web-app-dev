import math
def countFactors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count






max = 500
triNum = 1
sumTriNum = 0

while True:
    if countFactors(sumTriNum) >= max:
        print(sumTriNum)
        break
    else:
        sumTriNum += triNum
    triNum += 1