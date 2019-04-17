from tkinter import *
from game1.utilities import *
from game1.VistaJuegoLetras import *

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
    
    self.btn1 = Button(self.rootWindow, text="INICIAR NIVEL", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarLetras)
    self.btn1.pack()
    self.btn1.place(anchor=CENTER, x = XY-55, y = XY-17, width = 105) 

    self.labelcuatro = Label (self.rootWindow, text = "Este nivel tiene 6 rondas en total, en las cuales", bg = "white")
    self.labelcuatro.config(font=("Arial", 10))
    self.labelcuatro.pack()
    self.labelcuatro.place(anchor=W, x = 2, y = 80)
    self.labelcinco = Label (self.rootWindow, text = "se verá en el recuadro izquierdo una Vocal y en el", bg = "white")
    self.labelcinco.config(font=("Arial", 10))
    self.labelcinco.pack()
    self.labelcinco.place(anchor=W, x = 2, y = 100)
    self.labeluno = Label (self.rootWindow, text = "recuadro derecho una consonante. El juego", bg = "white")
    self.labeluno.config(font=("Arial", 10))
    self.labeluno.pack()
    self.labeluno.place(anchor=W, x = 2, y = 120)
    self.labeldos = Label (self.rootWindow, text = "consiste en presionar el botón [Z] cuando", bg = "white")
    self.labeldos.config(font=("Arial", 10))
    self.labeldos.pack()
    self.labeldos.place(anchor=W, x = 2, y = 140)
    self.labeltres = Label (self.rootWindow, text = "aparezca una consonante en el lado derecho y el", bg = "white")
    self.labeltres.config(font=("Arial", 10))
    self.labeltres.pack()
    self.labeltres.place(anchor=W, x = 2, y = 160)
    self.labelseis = Label (self.rootWindow, text = "botón [-] cuando aparezca una vocal en el lado", bg = "white")
    self.labelseis.config(font=("Arial", 10))
    self.labelseis.pack()
    self.labelseis.place(anchor=W, x = 2, y = 180)
    self.labelsiete = Label (self.rootWindow, text = "izquierdo. Si la letra aparece en el lado contrario", bg = "white")
    self.labelsiete.config(font=("Arial", 10))
    self.labelsiete.pack()
    self.labelsiete.place(anchor=W, x = 2, y = 200)
    self.labelocho = Label (self.rootWindow, text = "se debe esperar (4) segundos sin presionar", bg = "white")
    self.labelocho.config(font=("Arial", 10))
    self.labelocho.pack()
    self.labelocho.place(anchor=W, x = 2, y = 220)
    self.labelnueve = Label (self.rootWindow, text = "ningún botón, de lo contrario será contado como", bg = "white")
    self.labelnueve.config(font=("Arial", 10))
    self.labelnueve.pack()
    self.labelnueve.place(anchor=W, x = 2, y = 240)
    self.labeldiez = Label (self.rootWindow, text = "un error.", bg = "white")
    self.labeldiez.config(font=("Arial", 10))
    self.labeldiez.pack()
    self.labeldiez.place(anchor=W, x = 2, y = 260)

    self.rootWindow.mainloop()
  
  def iniciarLetras(self):
    self.rootWindow.destroy()
    letras = VistaJuegoLetras(self.parentWindow)
