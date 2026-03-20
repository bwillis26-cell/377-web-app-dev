from sys import argv
import random
import tkinter as tk



def random_password():
    SPECIALS = "!@#$%^&*()_-+={}[]:;><,./?"

    if len(argv) == 3:
        length = int(argv[1])
        checkDigits = "0" in argv[2]
        checkLower = "a" in argv[2]
        checkUpper = "A" in argv[2]
        checkSpecial = "!" in argv[2]
    elif len(argv) == 1:
        length = int(entry1.get())
        checkUpper = var1.get() == 1
        checkLower = var2.get() == 1
        checkDigits = var3.get() == 1
        checkSpecial = var4.get() == 1



        # length = int(input("How many characters are required? "))
        # checkDigits = input("Does your password require digits?(Y/N) ").upper()[0] == "Y"
        # checkSpecial = input("Does your password require special characters?(Y/N) ").upper()[0] == "Y"
        # checkUpper = input("Does your password require an uppercase letter?(Y/N) ").upper()[0] == "Y"
        # checkLower = input("Does your password require a lowercase letter?(Y/N) ").upper()[0] == "Y"
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


    messageVar.configure(text="".join(password))
root = tk.Tk()

entry1 = tk.Entry(root)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()



tk.Entry(root, text="Length").grid(row=0, column=1)
tk.Checkbutton(root, text="Capital", variable=var1).grid(row=1, sticky=tk.W)
tk.Checkbutton(root, text="Lowercase", variable=var2).grid(row=2, sticky=tk.W)
tk.Checkbutton(root, text="Digits", variable=var3).grid(row=3, sticky=tk.W)
tk.Checkbutton(root, text="Special", variable=var4).grid(row=4, sticky=tk.W)
entry1.grid(row=0, column=1)


ourMessage = ""
messageVar = tk.Message(root, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.grid(row=6, column=0, columnspan=2)

tk.Button(root, text="Get Random Password", width=25, command=random_password).grid(row=5, column=0, columnspan=2)

root.mainloop()