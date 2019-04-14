from tkinter import *
from config import *
from game1.ControlInhibitorio import ControlInhibitorio

class Juegos:
  def __init__(self):
    self.rootWindow = Tk()
    
    self.rootWindow.title("Juegos")
    self.rootWindow.config(heigh=XY, width=XY)
    self.rootWindow.configure(bg='white')

    windowWidth = self.rootWindow.winfo_reqwidth()
    windowHeight = self.rootWindow.winfo_reqheight()
    
    positionRight = int(self.rootWindow.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.rootWindow.winfo_screenheight()/2 - windowHeight/2)
    
    self.rootWindow.geometry("+{}+{}".format(positionRight, positionDown))

    title = Label(self.rootWindow, text = "MENÚ DE JUEGOS", bg = "white")
    title.config(font=("Righteous", 15))
    title.pack()
    title.place(anchor=CENTER, x=XY/2, y= (XY/4))

    btn1 = Button(self.rootWindow, text="Control Inhibitorio", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarControlI)
    btn1.pack()
    btn1.place(anchor=CENTER, x = (XY/2), y = (XY/2)-35, width = BTNSIZE) 
    btn2 = Button(self.rootWindow, text="Velocidad de Procesamiento", bg = RED, fg = "white", relief = GROOVE, font=("Arial", 11))
    btn2.pack()
    btn2.place(anchor=CENTER, x = XY/2, y = XY/2, width = BTNSIZE)
    btn3 = Button(self.rootWindow, text="Memoria de Trabajo Fonológica", bg = GREEN, fg = "white", relief = GROOVE, font=("Arial", 11))
    btn3.pack()
    btn3.place(anchor=CENTER, x = (XY/2), y = (XY/2)+35, width = BTNSIZE )

    self.rootWindow.mainloop()

  def iniciarControlI(self):
    self.rootWindow.withdraw()
    ctrlI = ControlInhibitorio(self.rootWindow)