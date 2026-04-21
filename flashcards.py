from tkinter import *
#from tkinter import colorchooser
from random import randint

root = Tk()
root.title("Flashcard App!")
root.geometry("400x400")
root.iconbitmap('/Users/eugene.lampione/Documents/repos/tkinter-python-programming/paw.ico')


# create function to determine add answer correct?
def add_correct(num_1,num_2):
    # calculate the actual answer
    correctAnswer = num_1 + num_2

    # correct incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set("Correct: " + str(num_1) + " + " + str(num_2) + " = " + str(correctAnswer))
    outputAnswerIncorrect.set("Incorrect: " + str(num_1) + " + " + str(num_2) + " = " + str(correctAnswer) + ", Not " + str(addAnswer.get()))

    if int(addAnswer.get()) == correctAnswer:
        addCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        addCorrectLabel.config(text=outputAnswerIncorrect.get())

    # clear the answer box
    addAnswer.delete(0, "end")

    # generate 2 new random numbers
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    addFlash.config(text=str(num1.get()) + " + " + str(num2.get()), font=("Helvetica", 72))

# def addition function
def add():
    hideMenuFrame()
    addFrame.pack(fill="both", expand=1)

    # create 2 random numbers
    global num1
    global num2

    num1 = IntVar()
    num2 = IntVar()

    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # put random numbers on the screen
    global addFlash
    addFlash = Label(addFrame, text=str(num1.get()) + " + " + str(num2.get()), font=("Helvetica", 72))
    addFlash.pack(pady=10)

    # answer box
    global addAnswer
    addAnswer = Entry(addFrame)
    addAnswer.pack(pady=5)

    # answer button
    answerButton = Button(addFrame, text="Answer", command=lambda: add_correct(num1.get(),num2.get()))
    answerButton.pack(pady=5)

    # correct or incorrect message
    global addCorrectLabel
    addCorrectLabel = Label(addFrame, text= "")
    addCorrectLabel.pack(pady=5)

# create function to determine subtract answer correct?
def subtract_correct(num_1,num_2):
    # calculate the actual answer
    correctAnswer = num_1 - num_2

    # correct incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set("Correct: " + str(num_1) + " - " + str(num_2) + " = " + str(correctAnswer))
    outputAnswerIncorrect.set("Incorrect: " + str(num_1) + " - " + str(num_2) + " = " + str(correctAnswer) + ", Not " + str(subtractAnswer.get()))

    if int(subtractAnswer.get()) == correctAnswer:
        subtractCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        subtractCorrectLabel.config(text=outputAnswerIncorrect.get())

    # clear the answer box
    subtractAnswer.delete(0, "end")

    # generate 2 new random numbers
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    subtractFlash.config(text=str(num1.get()) + " - " + str(num2.get()), font=("Helvetica", 72))

# def subtract function
def subtract():
    hideMenuFrame()
    subtractFrame.pack(fill="both", expand=1)

    # create 2 random numbers
    global num1
    global num2

    num1 = IntVar()
    num2 = IntVar()

    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # put random numbers on the screen
    global subtractFlash
    subtractFlash = Label(subtractFrame, text=str(num1.get()) + " - " + str(num2.get()), font=("Helvetica", 72))
    subtractFlash.pack(pady=10)

    # answer box
    global subtractAnswer
    subtractAnswer = Entry(subtractFrame)
    subtractAnswer.pack(pady=5)

    # answer button
    answerButton = Button(subtractFrame, text="Answer", command=lambda: subtract_correct(num1.get(),num2.get()))
    answerButton.pack(pady=5)

    # correct or incorrect message
    global subtractCorrectLabel
    subtractCorrectLabel = Label(subtractFrame, text= "")
    subtractCorrectLabel.pack(pady=5)

# create function to determine multiply answer correct?
def multiply_correct(num_1,num_2):
    # calculate the actual answer
    correctAnswer = num_1 * num_2

    # correct incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set("Correct: " + str(num_1) + " * " + str(num_2) + " = " + str(correctAnswer))
    outputAnswerIncorrect.set("Incorrect: " + str(num_1) + " * " + str(num_2) + " = " + str(correctAnswer) + ", Not " + str(multiplyAnswer.get()))

    if int(multiplyAnswer.get()) == correctAnswer:
        multiplyCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        multiplyCorrectLabel.config(text=outputAnswerIncorrect.get())

    # clear the answer box
    multiplyAnswer.delete(0, "end")

    # generate 2 new random numbers
    num1.set(randint(0,10))
    num2.set(randint(0,10))
    multiplyFlash.config(text=str(num1.get()) + " * " + str(num2.get()), font=("Helvetica", 72))

# def multiply function
def multiply():
    hideMenuFrame()
    multiplyFrame.pack(fill="both", expand=1)

    # create 2 random numbers
    global num1
    global num2

    num1 = IntVar()
    num2 = IntVar()

    num1.set(randint(0,10))
    num2.set(randint(0,10))

    # put random numbers on the screen
    global multiplyFlash
    multiplyFlash = Label(multiplyFrame, text=str(num1.get()) + " * " + str(num2.get()), font=("Helvetica", 72))
    multiplyFlash.pack(pady=10)

    # answer box
    global multiplyAnswer
    multiplyAnswer = Entry(multiplyFrame)
    multiplyAnswer.pack(pady=5)

    # answer button
    answerButton = Button(multiplyFrame, text="Answer", command=lambda: multiply_correct(num1.get(),num2.get()))
    answerButton.pack(pady=5)

    # correct or incorrect message
    global multiplyCorrectLabel
    multiplyCorrectLabel = Label(multiplyFrame, text= "")
    multiplyCorrectLabel.pack(pady=5)

# create function to determine divide answer correct?
def divide_correct(num_1,num_2):
    # calculate the actual answer
    correctAnswer = num_1 // num_2

    # correct incorrect message
    outputAnswerCorrect = StringVar()
    outputAnswerIncorrect = StringVar()
    outputAnswerCorrect.set("Correct: " + str(num_1) + " / " + str(num_2) + " = " + str(correctAnswer))
    outputAnswerIncorrect.set("Incorrect: " + str(num_1) + " / " + str(num_2) + " = " + str(correctAnswer) + ", Not " + str(divideAnswer.get()))

    if float(divideAnswer.get()) == correctAnswer:
        divideCorrectLabel.config(text=outputAnswerCorrect.get())
    else:
        divideCorrectLabel.config(text=outputAnswerIncorrect.get())

    # clear the answer box
    divideAnswer.delete(0, "end")

    # generate 2 new random numbers
    # ensure second number is not 0 and num 1 is divisible by num2
    num1.set(randint(0,100))
    num2.set(randint(1,100))
    
    while num1.get() % num2.get() != 0:
        # get new numbers
        num1.set(randint(0,100))
        num2.set(randint(1,100))
    
    divideFlash.config(text=str(num1.get()) + " / " + str(num2.get()), font=("Helvetica", 72))

# def division function
def divide():
    hideMenuFrame()
    divideFrame.pack(fill="both", expand=1)

    # create 2 random numbers
    global num1
    global num2

    num1 = IntVar()
    num2 = IntVar()
    num1.set(randint(0,100))
    num2.set(randint(1,100))

    # ensure second number is not 0 and num 1 is divisible by num2
    while num1.get() % num2.get() != 0:
        # get new numbers
        num1.set(randint(0,100))
        num2.set(randint(1,100))

    # put random numbers on the screen
    global divideFlash
    divideFlash = Label(divideFrame, text=str(num1.get()) + " / " + str(num2.get()), font=("Helvetica", 72))
    divideFlash.pack(pady=10)

    # answer box
    global divideAnswer
    divideAnswer = Entry(divideFrame)
    divideAnswer.pack(pady=5)

    # answer button
    answerButton = Button(divideFrame, text="Answer", command=lambda: divide_correct(num1.get(),num2.get()))
    answerButton.pack(pady=5)

    # correct or incorrect message
    global divideCorrectLabel
    divideCorrectLabel = Label(divideFrame, text= "")
    divideCorrectLabel.pack(pady=5)

# create hide frame function
def hideMenuFrame():
    # destroy children widget for each frame
    for widget in addFrame.winfo_children():
        widget.destroy()

    for widget in subtractFrame.winfo_children():
        widget.destroy()

    for widget in multiplyFrame.winfo_children():
        widget.destroy()

    for widget in divideFrame.winfo_children():
        widget.destroy()

    for widget in startFrame.winfo_children():
        widget.destroy()

    # hide all frames
    addFrame.pack_forget()
    subtractFrame.pack_forget()
    multiplyFrame.pack_forget()
    divideFrame.pack_forget()
    startFrame.pack_forget()

# start screen
def home():
    hideMenuFrame()
    startFrame.pack(fill="both", expand=1)
    startLabel = Label(startFrame, text="Welcome to Math Flashcards", font=("Helvetica",18)).pack(pady=20)

    # buttons to flash cards
    addButton = Button(startFrame, text="Addition Flashcards", command=add).pack(pady=5)
    subtractButton = Button(startFrame, text="Subtraction Flashcards", command=subtract).pack(pady=5)
    multiplyButton = Button(startFrame, text="Multiplication Flashcards", command=multiply).pack(pady=5)
    divideButton = Button(startFrame, text="Division Flashcards", command=divide).pack(pady=5)

#def main menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create menu items
mathMenu = Menu(myMenu)
myMenu.add_cascade(label="Mathcards", menu=mathMenu)

mathMenu.add_command(label="Add", command=add)
mathMenu.add_command(label="Subtract", command=subtract)
mathMenu.add_command(label="Multiply", command=multiply)
mathMenu.add_command(label="Divide", command=divide)
mathMenu.add_separator()
mathMenu.add_command(label="Home", command=home)
mathMenu.add_command(label="Exit", command=root.quit)

# create math frames
addFrame = Frame(root, width=400, height=400)
subtractFrame = Frame(root, width=400, height=400)
multiplyFrame = Frame(root, width=400, height=400)
divideFrame = Frame(root, width=400, height=400)
startFrame = Frame(root, height=400, width=400)

# show the start screen
home()

root.mainloop()