from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

helloLabel = Label(root)

# submit function
def submit():
    global helloLabel
    clear()
    helloLabel = Label(root,text="Hello " + e.get())
    helloLabel.grid(row=3,column=0)

def clear():
    helloLabel.grid_forget()

# forget
inputLabel = Label(root, text="Enter your name: ").grid(row=0,column=0)

e = Entry(root)
e.grid(row=1,column=0)

submitButton = Button(root,text="Submit", command=submit).grid(row=2,column=0)
clearButton = Button(root,text="Clear",command=clear).grid(row=2,column=1)

root.mainloop()