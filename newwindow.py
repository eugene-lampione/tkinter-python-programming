from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

def openWindow():
    new = Toplevel()
    new.title("Second Window")
    new.geometry("200x200")

    #global myImage

    myLabel = Label(new,text="Look and my 2nd window").pack(pady=20)

    myImage = ImageTk.PhotoImage(Image.open("eugene.jpg"))
    imgLabel = Label(new, image=myImage)
    imgLabel.pack(pady=20)


    destroyButton = Button(new, text="Quit",command=new.destroy)
    destroyButton.pack(pady=10)

    # minimize original window
    #hideButton = Button(new,text="hide main window", command=root.iconify) 
    #showButton = Button(new,text="show main window", command=root.deiconify)

    # withdrawl original window
    hideButton = Button(new,text="Hide main window", command=root.withdraw) 
    showButton = Button(new,text="Show main window", command=root.deiconify)

    killOriginal = Button(new, text="Quit Original", command=root.destroy).pack()

    hideButton.pack()
    showButton.pack() 

    new.mainloop()

# new window
myButton = Button(root, text="Open 2nd Window.", command=openWindow).pack()

root.mainloop()