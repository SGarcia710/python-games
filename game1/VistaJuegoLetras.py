from game1.JuegoLetras import JuegoLetras
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from datetime import datetime, timedelta
from game1.utilities import *
from game1.ControlInhibitorio import *

class VistaJuegoLetras: 
  # tamaño de la ventana
  X = 1000
  Y = 700
  TIEMPO_RESP = 3 # 3000ms
  def __init__(self, parentWindow):
    self.juego = JuegoLetras()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("Control Inihibitorio")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.segundos = 0
    self.nivelActual = None
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

    self.botonZ = Button(self.root, text = "Z", bd = 1, relief = GROOVE, bg = RED , fg = "white", font=("Arial", 16), command = lambda: self.accionBoton('Z'))
    self.botonZ.pack()
    self.botonZ.place(anchor=CENTER, x = 300, y = self.Y-150, width = 150, heigh = 50)

    self.botonG = Button(self.root, text = "-", bd = 1, relief = GROOVE, bg = RED, fg = "white", font=("Arial", 16), command = lambda: self.accionBoton('-'))
    self.botonG.pack()
    self.botonG.place(anchor=CENTER, x = self.X-300, y = self.Y-150, width = 150, heigh = 50)
      
    self.pintarNivel()

    self.root.mainloop()
  
  def accionBoton(self, letra):
    self.nivelActual.presionarBoton(letra)
    self.reiniciar()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None:
      self.terminado = True
      self.crearResultados()
    else:
      nivelActualStr = "Nivel " +str(self.juego.indiceNivel )
      self.label1.config(text = nivelActualStr)
      letraStr = self.nivelActual.letra.letra

      if self.nivelActual.lado == self.nivelActual.IZQ:
        self.labelIzq.config(text=letraStr, fg = "black")
        self.labelDer.config(text='_', fg = "white")
      else: 
        self.labelIzq.config(text='_', fg = "white")
        self.labelDer.config(text=letraStr, fg = "black")
  
  def crearResultados(self):
    aciertos, fallos = self.juego.calcularResultados()
    stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos) + "."
    mbox.showinfo("Juego completado", stringMBOX)
    stringResultado = "[Nivel 2] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+"\n"
    guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()

  def reiniciar(self):
    self.segundos = 0
    self.pintarNivel()
    
  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(0.1)
      self.segundos += 0.1
      if self.segundos >= self.TIEMPO_RESP:
        self.reiniciar()