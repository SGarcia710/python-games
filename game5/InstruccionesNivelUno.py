from tkinter import *
from game5.utilities import *
from game5.Vista import *

class InstruccionesNivelUno:
  def __init__(self, window):
    self.rootWindow = Tk()
    self.parentWindow = window
    self.rootWindow.title("INSTRUCCIONES")
    self.rootWindow.config(heigh=XY, width=XY)
    self.rootWindow.configure(bg='white')

    self.windowWidth = self.rootWindow.winfo_reqwidth()
    self.windowHeight = self.rootWindow.winfo_reqheight()

    self.positionRight = int(self.rootWindow.winfo_screenwidth()/2 - self.windowWidth/2)
    self.positionDown = int(self.rootWindow.winfo_screenheight()/2 - self.windowHeight/2)

    self.rootWindow.geometry("+{}+{}".format(self.positionRight, self.positionDown))

    self.title = Label(self.rootWindow, text = "INSTRUCCIONES", bg = "white")
    self.title.config(font=("Righteous", 15))
    self.title.pack()
    self.title.place(anchor=CENTER, x=XY/2, y= (XY/8))
    
    self.btn1 = Button(self.rootWindow, text="INICIAR NIVEL", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = lambda: self.iniciarVista(1))
    self.btn1.pack()
    self.btn1.place(anchor=CENTER, x = XY-55, y = XY-17, width = 105) 
    self.btn2 = Button(self.rootWindow, text="INICIAR PRUEBA", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = lambda: self.iniciarVista(0))
    self.btn2.pack()
    self.btn2.place(anchor=CENTER, x = XY-170, y = XY-17, width = 120) 

    self.btn5 = Button(self.rootWindow, text="Atras", bg = DARK, fg = "white", relief = GROOVE, command = self.volverMenu)
    self.btn5.pack()
    self.btn5.place(anchor=CENTER, x = 30, y = XY-17, width = 50 )

    string1 = "Este juego consiste en ver y recordar el recorrido"
    string2 = "que hace la rana. El jugador deberá presionar los"
    string3 = "nenufares(hojas) correspondientes al camino"
    string4 = "correcto. El camino debe seguir el orden mostrado"
    string5 = " al inicio de cada ronda, de lo contrario, cada"
    string6 = "paso que no siga el orden, será un error."

    self.labelcuatro = Label (self.rootWindow, text = string1, bg = "white")
    self.labelcuatro.config(font=("Arial", 10))
    self.labelcuatro.pack()
    self.labelcuatro.place(anchor=W, x = 2, y = 100)
    self.labelcinco = Label (self.rootWindow, text = string2, bg = "white")
    self.labelcinco.config(font=("Arial", 10))
    self.labelcinco.pack()
    self.labelcinco.place(anchor=W, x = 2, y = 120)
    self.labeluno = Label (self.rootWindow, text = string3, bg = "white")
    self.labeluno.config(font=("Arial", 10))
    self.labeluno.pack()
    self.labeluno.place(anchor=W, x = 2, y = 140)
    self.labeldos = Label (self.rootWindow, text = string4, bg = "white")
    self.labeldos.config(font=("Arial", 10))
    self.labeldos.pack()
    self.labeldos.place(anchor=W, x = 2, y = 160)
    self.labeltres = Label (self.rootWindow, text = string5, bg = "white")
    self.labeltres.config(font=("Arial", 10))
    self.labeltres.pack()
    self.labeltres.place(anchor=W, x = 2, y = 180)
    self.labelseis = Label (self.rootWindow, text = string6, bg = "white")
    self.labelseis.config(font=("Arial", 10))
    self.labelseis.pack()
    self.labelseis.place(anchor=W, x = 2, y = 200)

    self.rootWindow.mainloop()
  
  def iniciarVista(self, tipoJuego):
    self.rootWindow.destroy()
    dos = Vista(self.parentWindow, tipoJuego)
  
  def volverMenu(self):
    self.rootWindow.destroy()
    self.parentWindow.deiconify()