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
import time

class VistaJuegoLetras: 
  # tamaño de la ventana
  X = 1000
  Y = 700
  TIEMPOESPERA = 4 # tiempo de espera cuando hay trampa.
  def __init__(self, parentWindow):
    self.juego = JuegoLetras()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("Control Inihibitorio")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.tiempoActual = None
    self.segundos = 0
    self.terminado = False
    self.hilo2 = threading.Thread(target=self.ejecutarCronometro)
    self.hilo2.start()
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
    if nivel is None:
      self.terminado = True
      cadenaLog, cadenaMsg = self.crearResultado()
      mbox.showinfo("Juego completado!", cadenaMsg)
      guardarLog(cadenaLog)
      self.root.destroy()
      self.parentWindow.deiconify()
    else:
      self.botonG.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA2))
      self.botonZ.configure(command= lambda: self.presionarBoton(nivel,nivel.TECLA1))
      self.tiempoActual = self.segundos
      nivelActualStr = "Nivel " +str(nivel.numNivel)
      self.label1.config(text = nivelActualStr)
      letraStr = nivel.letra.letra

      if nivel.lado == nivel.IZQ:
        self.labelIzq.config(text=letraStr, fg = "black")
        self.labelDer.config(text='_', fg = "white")
      else: 
        self.labelIzq.config(text='_', fg = "white")
        self.labelDer.config(text=letraStr, fg = "black")

      if nivel.trampa:
        hilo1 = threading.Thread(target=self.ejecutarPausa)
        hilo1.start()

  def ejecutarPausa(self):
    time.sleep(self.TIEMPOESPERA)
    self.mostrarMensaje()

  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(1)
      self.segundos += 1

  def presionarBoton(self,nivel,tecla):
    nivel.presionarBoton(tecla)
    ahora = self.segundos
    transcurrido = ahora - self.tiempoActual
    nivel.tiempoReaccion = transcurrido

    if not nivel.trampa:
      self.mostrarMensaje()

  def mostrarMensaje(self):
    mbox.showinfo("Felicitaciones!", "Nivel terminado.")
    self.pintarNivel()

  def crearResultado(self):
    cadenaLog = "[Nivel 2] Fecha: " + self.fechaInicio + ","
    cadenaMsg = "Fecha: " + self.fechaInicio + "\n"
    niveles = self.juego.nivelesJuego
    for nivel in niveles:
      tiempoR = nivel.tiempoReaccion
      segundos = 0
      minutos = 0
      if tiempoR is not None:
        segundos = tiempoR % 60
        minutos = int(tiempoR / 60)
      resultado = None
      if nivel.trampa == True:
        if nivel.botonPresionado == None:
          resultado = "Acierto"
        else:
          resultado = "Error"
      else:
        if nivel.lado == nivel.IZQ and nivel.letra.tipoLetra == nivel.letra.VOCAL:
          if nivel.botonPresionado == nivel.TECLA1:
            resultado = "Acierto"
          else:
            resultado = "Error" 
        else:
          if nivel.lado == nivel.DER and nivel.letra.tipoLetra == nivel.letra.CONSONANTE:
            if nivel.botonPresionado == nivel.TECLA2:
              resultado = "Acierto"
            else:
              resultado = "Error"
        
      if nivel.trampa:
        cadenaLog += " T.R." + str(nivel.numNivel) + " Minutos: 0, Segundos: 0 Resultado: " + resultado + ","
        cadenaMsg += "T.R." + str(nivel.numNivel) + " 0:0 " + resultado + "\n"
      else:
        cadenaLog += " T.R." + str(nivel.numNivel) + " Minutos: " + str(minutos) + " Segundos: " + str(segundos) + " Resultado: " + resultado + ","
        cadenaMsg += "T.R." + str(nivel.numNivel) + " " + str(minutos) + ":" + str(segundos) + " " + resultado + "\n"
    cadenaLog = cadenaLog[0: len(cadenaLog) - 1]+"\n"
    return cadenaLog, cadenaMsg