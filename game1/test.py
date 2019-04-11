from tkinter import *
from tkinter import PhotoImage

def print_hello():
    print('hello')

root = Tk()
root.geometry("960x600")

imagetest = PhotoImage(file="blue.png")

button_qwer = Button(root, text="asdfasdf", image=imagetest, command=print_hello)
button_qwer.pack()   # <-- don't forget to place the button in the window

root.mainloop()