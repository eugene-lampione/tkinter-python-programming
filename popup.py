from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

# create popup function
def popup():
    response = messagebox.askokcancel("Popup Title", "Look at my popup message!!")
    responseLabel = Label(root, text=response).pack(pady=10)

    '''
    if response == 1:
        responseLabel = Label(root, text="you clicked yes!").pack(pady=10)
    else:
        responseLabel = Label(root, text="you clicked no!").pack(pady=10)
    '''

# popup boxes
# showinfo (returns ok), showwarning (returns ok), showerror (returns ok), askquestion (yes=yes,no=no), askokcancel (ok=1,cancel=0), askyesno (yes=1,no=0)
popButton = Button(root, text="Click to Pop up!", command=popup)
popButton.pack(pady=20)

root.mainloop()