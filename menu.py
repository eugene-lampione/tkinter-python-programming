from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
#/Users/eugene.lampione/Documents/repos/tkinter-python-programming
# /Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico
root.iconbitmap('/Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico')

def fakeCommand():
    pass

def show():
    myFrame.grid(row=1, column=0, columnspan=2,padx=20,pady=20)

def hide():
    myFrame.grid_forget()

# define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=fakeCommand)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# create another submenu
editMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut",command=fakeCommand)
editMenu.add_command(label="Copy",command=fakeCommand)
editMenu.add_command(label="Paste",command=fakeCommand)

# frames are a way to group things together.
# create button
showButton = Button(root, text="Show", command=show)
hideButton = Button(root, text="Hide", command=hide)
showButton.grid(row=0,column=0)
hideButton.grid(row=0, column=1)

myFrame = Frame(root, width=200, height=200, bd=5,bg="blue", relief="sunken")
myFrame.grid(row=1, column=0, columnspan=2,padx=20,pady=20)

frameLabel = Label(myFrame, text="Hello World!", font=("Helveltica", 20))
frameLabel.pack(padx=20,pady=20)

root.mainloop()