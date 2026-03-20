import tkinter as tk

def on_click():
    messageVar.configure(text="Hello " + entry1.get() + " " + entry2.get())


root = tk.Tk()
tk.Label(root, text="First Name").grid(row=1, column=0)
tk.Label(root, text="Last Name").grid(row=2, column=0)

var1 = tk.IntVar()
var2 = tk.IntVar()
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

tk.Checkbutton(root, text="Male", variable=var1).grid(row=3, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=4, sticky=tk.W)
tk.Button(root, text="Do Something", width=25, command=on_click).grid(row=5, column=0, columnspan=2)

ourMessage = "Hello"
messageVar = tk.Message(root, text=ourMessage)
messageVar.config(bg="lightgreen")
messageVar.grid(row=0, column=0, columnspan=2)







root.mainloop()
