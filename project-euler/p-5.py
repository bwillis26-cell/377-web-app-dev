num = 21
check = False

while not check:
    for i in range(1, 21):
        if num % i != 0:
            check = False
            break
    num += 1
    print(num)