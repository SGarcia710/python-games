from tkinter import *
from game2.utilities import *
from game2.VistaJuegoVelPro import *
from game2.JuegoProcesamiento import *

class InstruccionesNivelDos:
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

    self.title = Label(self.rootWindow, text = "INSTRUCCIONES NIVEL 2", bg = "white")
    self.title.config(font=("Righteous", 15))
    self.title.pack()
    self.title.place(anchor=CENTER, x=XY/2, y= (XY/8))
    
    self.btn1 = Button(self.rootWindow, text="INICIAR NIVEL", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarVista)
    self.btn1.pack()
    self.btn1.place(anchor=CENTER, x = XY-55, y = XY-17, width = 105) 

    self.btn5 = Button(self.rootWindow, text="Atras", bg = DARK, fg = "white", relief = GROOVE, command = self.volverMenu)
    self.btn5.pack()
    self.btn5.place(anchor=CENTER, x = 30, y = XY-17, width = 50 )

    string1 = "Este nivel tiene 6 rondas, en las cuales el"
    string2 = "jugador deberá presionar el botón [Z] cuando"
    string3 = "la letra corresponda a la inicial de alguno de"
    string4 = "los elementos contenidos en cualquiera de las"
    string5 = "tres ilustraciones o [-] en caso contrario."
    string6 = ""

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
  
  def iniciarVista(self):
    self.rootWindow.destroy()
    dos = VistaJuegoVelPro(self.parentWindow, VelocidadProcesamiento.JUEGO_DOS)
  
  def volverMenu(self):
    self.rootWindow.destroy()
    self.parentWindow.deiconify()