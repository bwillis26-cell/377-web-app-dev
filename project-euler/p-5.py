num = 21
check = False

while not check:
    if (num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0):
        check = True
        print(num)
    else:
        num += 1


# num = 2520
# check = False


# while not check:
#     for i in range(1, 21):
#         if num % i == 0:
#             check = False
#             break
#         else:
#             check = True
#     if check:
#         print(num)
#     else:
#         num += 2520
    
    