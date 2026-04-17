from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

def select():
    myLabel = Label(root,text=myCombo.get()).pack(pady=10)

# combo boxes (dropdown)
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
]

myCombo = ttk.Combobox(root,value=options)
myCombo.current(0)
myCombo.pack(pady=10)

myButton = Button(root,text="Select",command=select).pack()


root.mainloop()