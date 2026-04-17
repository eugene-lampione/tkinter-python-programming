from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

# create radio function
def radio():
    if v.get() == "one":
        answerLabel = Label(root, text="You clicked radio button One!")
    else:
        answerLabel = Label(root, text="You clicked radio button Two!")
    
    answerLabel.pack(pady=20)

# radio buttons
v = StringVar()
v.set("one")

rbutton1 = Radiobutton(root, text="One", variable=v, value="one").pack()
rbutton2 = Radiobutton(root, text="Two", variable=v, value="two").pack()

submitButton = Button(root,text="Submit", command=radio)
submitButton.pack(pady=20)


root.mainloop()