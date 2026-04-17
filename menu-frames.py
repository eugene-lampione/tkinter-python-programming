from tkinter import *

root = Tk()
root.title("Hello World!")
#root.geometry("400x400")
#/Users/eugene.lampione/Documents/repos/tkinter-python-programming
# /Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico
root.iconbitmap('/Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico')

def fakeCommand():
    pass

def new():
    hideMenuFrames()
    currentStatus.set("file status!")
    fileFrame.grid(row=0, column=0, columnspan=2,padx=20,pady=20)

def cut():
    hideMenuFrames()
    currentStatus.set("Cut Status!")
    editFrame.grid(row=0, column=0, columnspan=2,padx=20,pady=20)

def show():
    myFrame.grid(row=1, column=0, columnspan=2,padx=20,pady=20)

def hideMenuFrames():
    editFrame.grid_forget()
    fileFrame.grid_forget()

# define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=new)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# create another submenu
editMenu = Menu(myMenu)
myMenu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=fakeCommand)
editMenu.add_command(label="Paste",command=fakeCommand)

# frames are a way to group things together.
# create button
'''
showButton = Button(root, text="Show", command=show)
hideButton = Button(root, text="Hide", command=hide)
showButton.grid(row=0,column=0)
hideButton.grid(row=0, column=1)
'''

# file Menu Frame
fileFrame = Frame(root, width=200, height=200, bd=5,bg="blue", relief="sunken")
#fileFrame.grid(row=1, column=0, columnspan=2,padx=20,pady=20)
fileFrameLabel = Label(fileFrame, text="FILE FRAME!", font=("Helveltica", 20))
fileFrameLabel.pack(padx=20,pady=20)

# Edit Menu Frame
editFrame = Frame(root, width=200, height=200, bd=5,bg="blue", relief="sunken")
#fileFrame.grid(row=1, column=0, columnspan=2,padx=20,pady=20)
editFrameLabel = Label(editFrame, text="CUT FRAME!", font=("Helveltica", 20))
editFrameLabel.pack(padx=20,pady=20)

currentStatus = StringVar()
currentStatus.set("Waiting!")

myStatus = Label(root,textvariable=currentStatus, bd=2, relief="sunken", width=50, anchor=E)
myStatus.grid(row=1, column=0)


root.mainloop()