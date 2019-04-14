from tkinter import *
from game1.utilities import *
from game1.VistaJuegoGlobos import *

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

    self.title = Label(self.rootWindow, text = "INSTRUCCIONES NIVEL 1", bg = "white")
    self.title.config(font=("Righteous", 15))
    self.title.pack()
    self.title.place(anchor=CENTER, x=XY/2, y= (XY/8))
    
    self.btn1 = Button(self.rootWindow, text="INICIAR NIVEL", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarGlobos)
    self.btn1.pack()
    self.btn1.place(anchor=CENTER, x = XY-55, y = XY-17, width = 105) 

    self.labelcuatro = Label (self.rootWindow, text = "Este nivel tiene 3 niveles de dificultad, los cuales", bg = "white")
    self.labelcuatro.config(font=("Arial", 10))
    self.labelcuatro.pack()
    self.labelcuatro.place(anchor=W, x = 2, y = 100)
    self.labelcinco = Label (self.rootWindow, text = "harán variar el número de globos rojos mostrados.", bg = "white")
    self.labelcinco.config(font=("Arial", 10))
    self.labelcinco.pack()
    self.labelcinco.place(anchor=W, x = 2, y = 120)
    self.labeluno = Label (self.rootWindow, text = "El juego consiste en dar clic en cada globo Rojo", bg = "white")
    self.labeluno.config(font=("Arial", 10))
    self.labeluno.pack()
    self.labeluno.place(anchor=W, x = 2, y = 140)
    self.labeldos = Label (self.rootWindow, text = "que aparezca en la pantalla.", bg = "white")
    self.labeldos.config(font=("Arial", 10))
    self.labeldos.pack()
    self.labeldos.place(anchor=W, x = 2, y = 160)
    self.labeltres = Label (self.rootWindow, text = "El jugador deberá ignorar los globos Azules o sino", bg = "white")
    self.labeltres.config(font=("Arial", 10))
    self.labeltres.pack()
    self.labeltres.place(anchor=W, x = 2, y = 180)
    self.labelseis = Label (self.rootWindow, text = "estos serán contados como errores.", bg = "white")
    self.labelseis.config(font=("Arial", 10))
    self.labelseis.pack()
    self.labelseis.place(anchor=W, x = 2, y = 200)

    self.rootWindow.mainloop()
  
  def iniciarGlobos(self):
    self.rootWindow.destroy()
    globos = VistaJuegoGlobos(self.parentWindow)