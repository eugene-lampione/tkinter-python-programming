from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
#/Users/eugene.lampione/Documents/repos/tkinter-python-programming
# /Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico
root.iconbitmap('/Users/eugene.lampione/Documents/repos/tkinter-python-programming/weight-icon-2455976-256.ico')

# create clicked function
def clicked():
    global myLabel2
    input = e.get()
    myLabel2 = Label(root, text="Hello " + input)
    myLabel2.pack()

def hide():
    myLabel2.pack_forget()
    # myLabel2.destroy()

def show():
    myLabel2.pack()


'''
# Add Images
myImage = ImageTk.PhotoImage(Image.open("IMG_3290.jpg"))
imageLabel = Label(image=myImage, width=300, height=300)
imageLabel.pack()
'''

# create label and put it on the screen
# pack is easier, just packs it on the screen.
# grid you can place it where you want
myLabel = Label(root, text="Enter your Name: ")
myLabel.pack()

# create an entry widget
e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

# create button
myButton = Button(root, text="Click Me!", command=clicked)
myButton.pack(pady=20)

# create button
hideButton = Button(root, text="Hide", command=hide)
hideButton.pack(pady=20)

# create button
showButton = Button(root, text="Show", command=show)
showButton.pack(pady=20)


'''
grid options
sticky = N, E, S, W
rowspan
columnspan
'''


















root.mainloop()