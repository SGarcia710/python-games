from game3.JuegoSonidos import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game3.utilities import *
import os
from pygame import mixer

class VistaMemoriaTrabajoFonologica: 
  # tamaño de la ventana
  X = 800
  Y = 500
  def __init__(self, parentWindow):
    self.juego = JuegoSonidos()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("Velocidad Procesamiento")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None
    self.segundos = 0
    self.terminado = False
    self.root.resizable(width=False, height=False)

    windowWidth = self.root.winfo_reqwidth()
    windowHeight = self.root.winfo_reqheight()

    positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
    
    self.root.geometry("+{}+{}".format(positionRight, positionDown))

    self.nivelActualStr = "Nivel 1"
    self.label1 = Label(self.root, text = self.nivelActualStr)
    self.label1.config(font=("Righteous", 30), bg = "white")
    self.label1.pack()
    self.label1.place(anchor=CENTER, x=self.X/2, y= 50)

    self.btnReproducir = Button(self.root, text = "Reproducir", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 16),command= self.reproducir)
    self.btnReproducir.pack()
    self.btnReproducir.place(anchor=CENTER, x=self.X/2, y = 200, width = 150, heigh = 50)
    self.btnReproducir.config(state="normal")

    self.botones = []

    self.botonUno = Button(self.root, text = "Boton Uno", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)


    self.botonDos = Button(self.root, text = "Boton Dos", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonTres = Button(self.root, text = "Boton Tres", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonCuatro = Button(self.root, text = "Boton Cuatro", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonCinco = Button(self.root, text = "Boton Cinco", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonSeis = Button(self.root, text = "Boton Seis", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonSiete = Button(self.root, text = "Boton Siete", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.botonOcho = Button(self.root, text = "Boton Ocho", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 13),command= self.reproducir)

    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None:
      print("pendiente")
    else:
      self.label1.configure(text="Nivel " + str(self.nivelActual.numNivel))
      self.btnReproducir.config(state="normal")
      self.pintarBotones()

  def pintarBotones(self):
    if self.nivelActual.numNivel in [1,2]:
      self.botonUno.pack()
      self.botonUno.place(anchor=CENTER, x=(self.X/2)-240, y = 400, width = 150, heigh = 30)
      self.botonDos.pack()
      self.botonDos.place(anchor=CENTER, x=(self.X/2)-80, y = 400, width = 150, heigh = 30)
      self.botonTres.pack()
      self.botonTres.place(anchor=CENTER, x=(self.X/2)+80, y = 400, width = 150, heigh = 30)
      self.botonCuatro.pack()
      self.botonCuatro.place(anchor=CENTER, x=(self.X/2)+240, y = 400, width = 150, heigh = 30)
    elif self.nivelActual.numNivel in [3,4]:
      self.botonCinco.pack()
      self.botonCinco.place(anchor=CENTER, x=(self.X/2)-80, y = 450, width = 150, heigh = 30)
      self.botonSeis.pack()
      self.botonSeis.place(anchor=CENTER, x=(self.X/2)+80, y = 450, width = 150, heigh = 30)
    elif self.nivelActual.numNivel in [5,6]:
      self.botonSiete.pack()
      self.botonSiete.place(anchor=CENTER, x=(self.X/2)+80, y = 450, width = 150, heigh = 30)
      self.botonOcho.pack()
      self.botonOcho.place(anchor=CENTER, x=(self.X/2)+240, y = 450, width = 150, heigh = 30)
    else:
      print("Pendiente")

  def reproducir(self):
    self.btnReproducir.config(state="disabled")
    mixer.init()
    for sonido in self.nivelActual.sonidos:
      mixer.music.load(sonido.ruta)
      mixer.music.play()
      time.sleep(2)
    self.pintarNivel()
