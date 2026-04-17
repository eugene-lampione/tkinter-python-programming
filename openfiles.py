from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

def openImage():
    # open dialog box
    root.filename = filedialog.askopenfilename(initialdir="/Users/eugene.lampione/Documents/repos/tkinter-python-programming/", title="Open an Image", filetypes=( ("JPG Files", "*.jpg"), ("All Files","*.*") ))
    #myLabel = Label(root, text=root.filename).pack(pady=10)
    global myImage
    
    myImage = ImageTk.PhotoImage(Image.open(root.filename))
    imgLabel = Label(root, image=myImage)
    imgLabel.pack(pady=20)


myButton = Button(root, text="Open Image", command=openImage).pack(pady=10)

root.mainloop()