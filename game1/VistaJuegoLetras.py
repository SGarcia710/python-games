from game1.JuegoLetras import JuegoLetras
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from datetime import datetime, timedelta
from game1.utilities import *
from game1.ControlInhibitorio import *
import time, threading
import tkinter.messagebox as mbox
from datetime import datetime

class VistaJuegoLetras: 
  X = 1000
  Y = 700
  def __init__(self,parentWindow):
    self.juego = JuegoLetras()
    self.root = Toplevel()#cambiar por TopLevel()
    self.parentWindow = parentWindow
    self.root.title("Control Inihibitorio")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.tiempoActual = None
    self.root.resizable(width=False, height=False)

    windowWidth = self.root.winfo_reqwidth()
    windowHeight = self.root.winfo_reqheight()

    positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
    
    self.root.geometry("+{}+{}".format(positionRight, positionDown))

    # self.label1 = Label(self.root, text = "")
    # self.label1.config(font=("Righteous", 30), bg = "white")
    # self.label1.pack()
    # self.label1.place(anchor=CENTER, x=self.X/2, y= self.Y/6)

    # self.iniciarJuego()
    self.pintarNivel()

    self.root.mainloop()

  # def iniciarJuego(self):


  def pintarNivel(self):
    nivel = self.juego.obtenerNivel()

    if nivel is None:
      print("ano")
    else:
      self.tiempoActual = datetime.now()
      nivelActualStr = "Nivel "+str(nivel.numNivel)
      label1 = Label(self.root, text = nivelActualStr)
      label1.config(text = nivelActualStr)
      label1.pack()
      label1.place(anchor=CENTER, x=self.X/2, y= self.Y/6)
      letraStr = nivel.letra.letra
      if nivel.lado == nivel.IZQ:
        labelIzq = Label(self.root, text = letraStr)
        labelIzq.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15)
        labelIzq.pack()
        labelIzq.place(anchor=CENTER, x=200, y= self.Y/2)
        labelDer = Label(self.root, text = '_')
        labelDer.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15, fg = "white")
        labelDer.pack()
        labelDer.place(anchor=CENTER, x=self.X-200, y = self.Y/2)
      else: 
        labelIzq = Label(self.root, text = '_')
        labelIzq.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15, fg = "white")
        labelIzq.pack()
        labelIzq.place(anchor=CENTER, x=200, y= self.Y/2)
        labelDer = Label(self.root, text = letraStr)
        labelDer.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15)
        labelDer.pack()
        labelDer.place(anchor=CENTER, x=self.X-200, y = self.Y/2)
      
      botonZ = Button(self.root, text = "Z", bd = 1, relief = GROOVE, bg = RED , fg = "white", font=("Arial", 16))
      botonZ.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA1) )
      botonZ.pack()
      botonZ.place(anchor=CENTER, x = 300, y = self.Y-150, width = 150, heigh = 50)

      botonG = Button(self.root, text = "-", bd = 1, relief = GROOVE, bg = RED, fg = "white", font=("Arial", 16))
      botonG.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA2)  )
      botonG.pack()
      botonG.place(anchor=CENTER, x = self.X-300, y = self.Y-150, width = 150, heigh = 50)
      if nivel.trampa:
        hilo1 = threading.Thread(target=self.ejecutarPausa)
        hilo1.start()

  def ejecutarPausa(self):
    time.sleep(5)
    self.mostrarMensaje()


  def presionarBoton(self,nivel,tecla):
    nivel.presionarBoton(tecla)
    ahora = datetime.now()
    transcurrido = ahora - self.tiempoActual
    nivel.tiempoReaccion = transcurrido
    if not nivel.trampa:
      self.mostrarMensaje()
      

  def mostrarMensaje(self):
    mbox.showinfo("Felicitaciones!", "Nivel terminado.")
    self.pintarNivel()