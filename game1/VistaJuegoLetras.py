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
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
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

    self.label1 = Label(self.root, text = "")
    self.label1.config(font=("Righteous", 30), bg = "white")
    self.label1.pack()
    self.label1.place(anchor=CENTER, x=self.X/2, y= self.Y/6)

    self.labelIzq = Label(self.root, text = "letraStr")
    self.labelIzq.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15)
    self.labelIzq.pack()
    self.labelIzq.place(anchor=CENTER, x=200, y= self.Y/2)

    self.labelDer = Label(self.root, text = '_')
    self.labelDer.config(font=("Righteous", 50), bg = "white", bd = 2, relief = GROOVE, padx = 15, fg = "white")
    self.labelDer.pack()
    self.labelDer.place(anchor=CENTER, x=self.X-200, y = self.Y/2)

    self.botonZ = Button(self.root, text = "Z", bd = 1, relief = GROOVE, bg = RED , fg = "white", font=("Arial", 16))
    self.botonZ.pack()
    self.botonZ.place(anchor=CENTER, x = 300, y = self.Y-150, width = 150, heigh = 50)

    self.botonG = Button(self.root, text = "-", bd = 1, relief = GROOVE, bg = RED, fg = "white", font=("Arial", 16))
    self.botonG.pack()
    self.botonG.place(anchor=CENTER, x = self.X-300, y = self.Y-150, width = 150, heigh = 50)
      
    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    nivel = self.juego.obtenerNivel()

    self.botonG.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA2))
    self.botonZ.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA1))

    if nivel is None:
      cadenaLog, cadenaMsg = self.crearResultado()
      print(cadenaLog)
      print(cadenaMsg)

    else:
      self.tiempoActual = datetime.now()
      nivelActualStr = "Nivel " +str(nivel.numNivel)
      self.label1.config(text = nivelActualStr)
      letraStr = nivel.letra.letra

      if nivel.lado == nivel.IZQ:
        print("IZQ "+letraStr)
        self.labelIzq.config(text=letraStr, fg = "black")
        self.labelDer.config(text='_', fg = "white")
      else: 
        self.labelIzq.config(text='_', fg = "white")
        print("DER "+letraStr)
        self.labelDer.config(text=letraStr, fg = "black")

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

  def crearResultado(self):
    cadenaLog = "[Nivel 2]" + self.fechaInicio + ","
    niveles = self.juego.nivelesJuego
    for nivel in niveles:
      tiempoR = nivel.tiempoReaccion
      print(type(tiempoR))
      # strftime('%Y-%m-%d %H:%M:%S')
      segundos = tiempoR.seconds
      # minutos = tiempoR.minutes
      minutos = "0"
      resultado = None
      if nivel.trampa and nivel.botonPresionado  == None:
        resultado = "Acierto"
      elif not nivel.trampa and nivel.lado == nivel.IZQ and nivel.botonPresionado == nivel.IZQ:
        resultado = "Acierto"
      elif not nivel.trampa and nivel.lado == nivel.DER and nivel.botonPresionado == nivel.DER:
        resultado = "Acierto"
      else:
        resultado = "Error"

      if nivel.trampa:
        cadenaLog += " T.R." + nivel.numNivel + " 0:0 " + resultado + ","
      else:
        cadenaLog += " T.R." + nivel.numNivel + " " + minutos + ":" + segundos + " " + resultado + ","
    
    return cadenaLog, "Pendiente"