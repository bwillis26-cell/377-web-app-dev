count = 0
fibo1 = 1
fibo2 = 2
max = 4000000

print(fibo1)

while (fibo1 < max and fibo2 < max):
    if (fibo2 % 2 == 0):
        count += fibo2
    
    
    print(fibo2)

    temp = fibo1
    fibo1 = fibo2
    fibo2 += temp
    



print(count)