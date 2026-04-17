from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

def toppings():
    toppingsLabel = Label(root, text=v.get()).pack(pady=20)

# checkboxes
v = StringVar()

checkbutton1 = Checkbutton(root, text="Pepperoni",variable=v, onvalue="Pepperoni", offvalue="No Peppperoni")
checkbutton1.deselect()
checkbutton1.pack()
'''
checkbutton2 = Checkbutton(root, text="Meatball",variable=v, onvalue="Meatball", offvalue="No Meatball")
checkbutton2.deselect()
checkbutton2.pack()
'''

submitButton = Button(root, text="Select Toppings", command=toppings).pack(pady=20)

root.mainloop()