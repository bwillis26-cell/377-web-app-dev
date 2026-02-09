max = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        string1 = str(i * j)
        if string1 == string1[::-1]:
            temp = i * j
            if temp > max:
                max = temp


print(max)