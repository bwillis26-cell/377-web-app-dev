squareSum = 0
sumOfSquares = 0

for i in range(1, 101):
    squareSum += i
    sumOfSquares += i * i

squareSum **= 2

print(sumOfSquares - squareSum)