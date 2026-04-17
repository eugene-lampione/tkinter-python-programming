from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color Picker!")
root.geometry("400x400")
root.iconbitmap('/Users/eugene.lampione/Documents/repos/tkinter-python-programming/exe/paw.ico')

def color():
    myColor = colorchooser.askcolor()[1]
    myLabel = Label(root,text=myColor).pack(pady=10)
    myLabel2 = Label(root,text="You picked a color!!", font=("Helvetica",32), bg=myColor).pack(pady=10)

myButton = Button(root,text="Pick a Color", command=color).pack()

root.mainloop()

'''
To create an executable file use the following command
python3 -m PyInstaller --onefile --icon=[iconimage] --windowed [file to make executable]   

https://pyinstaller.org/en/stable/usage.html

-m <FILE or XML>
Deprecated shorthand for –manifest.
'''