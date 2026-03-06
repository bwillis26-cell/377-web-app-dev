from sys import argv
import random

SPECIALS = "!@#$%^&*()_-+={}[]:;><,./?"

if len(argv) == 3:
    length = int(argv[1])
    checkDigits = "0" in argv[2]
    checkLower = "a" in argv[2]
    checkUpper = "A" in argv[2]
    checkSpecial = "!" in argv[2]
elif len(argv) == 1:
    length = int(input("How many characters are required? "))
    checkDigits = input("Does your password require digits?(Y/N) ").upper()[0] == "Y"
    checkSpecial = input("Does your password require special characters?(Y/N) ").upper()[0] == "Y"
    checkUpper = input("Does your password require an uppercase letter?(Y/N) ").upper()[0] == "Y"
    checkLower = input("Does your password require a lowercase letter?(Y/N) ").upper()[0] == "Y"
else:
    print("Expected usage: password-generator.py LENGTH PATTERN")
    print("where pattern contains one or more of the following: Aa0!")
    exit()
# digitRandCheck = random.randint(0, length - 1)




password = []

if checkDigits:
    password.append(str(random.randint(0, 9)))
if checkUpper:
    password.append(chr(ord("A") + random.randint(0, 25)))
if checkLower:
    password.append(chr(ord("a") + random.randint(0, 25)))
if checkSpecial:
    password.append(SPECIALS[random.randint(0, len(SPECIALS) - 1)])


while len(password) < length:
    choice = random.randint(1, 4)


    if choice == 1 and checkDigits:
        password.append(str(random.randint(0, 9)))
    if choice == 2 and checkUpper:
        password.append(chr(ord("A") + random.randint(0, 25)))
    if choice == 3 and checkLower:
        password.append(chr(ord("a") + random.randint(0, 25)))
    if checkSpecial:
        password.append(SPECIALS[random.randint(0, len(SPECIALS) - 1)])



random.shuffle(password)


print("".join(password))

