from game4.JuegoCartas import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game4.utilities import *
import os
from pygame import mixer
from tinytag import TinyTag
import math

class VistaCartas: 
  # tamaño de la ventana
  X = 1000 
  Y = 700
  def __init__(self, parentWindow):
    self.juego = JuegoCartas()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("FLEX. COGNITIVA.")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None
    self.terminado = False
    self.segundos = 0
    self.root.resizable(width=False, height=False)
    self.hilo2 = threading.Thread(target=self.ejecutarCronometro)
    self.hilo2.start()

    self.imagesRoutes = []
    for e in self.juego.cartasBase:
      self.imagesRoutes.append(e.ruta)
    self.imageOne = PhotoImage(file= self.imagesRoutes[0])
    self.imageTwo = PhotoImage(file= self.imagesRoutes[1])
    self.imageThree = PhotoImage(file= self.imagesRoutes[2])
    self.imageFour = PhotoImage(file= self.imagesRoutes[3])

    self.imageLevel = PhotoImage(file="game4/assets/images/circulo,azul,1.png")
    
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
    
    self.boton1 = Button(self.root, image=self.imageOne,relief = RAISED,  bd = 0, bg = "white")
    self.boton1.configure(command = lambda: self.presionarBoton(self.imagesRoutes[0]))
    self.boton1.pack()
    self.boton1.place(anchor=CENTER, x = self.X/2-250, y = self.Y/2-100)
    self.boton2 = Button(self.root, image=self.imageTwo,relief = RAISED, bd = 0, bg = "white")
    self.boton2.configure(command = lambda: self.presionarBoton(self.imagesRoutes[1]))
    self.boton2.pack()
    self.boton2.place(anchor=CENTER, x = self.X/2-85, y = self.Y/2-100)
    self.boton3 = Button(self.root, image=self.imageThree,relief = RAISED, bd = 0, bg = "white")
    self.boton3.configure(command = lambda: self.presionarBoton(self.imagesRoutes[2]))
    self.boton3.pack()
    self.boton3.place(anchor=CENTER, x = self.X/2+85, y = self.Y/2-100)
    self.boton4 = Button(self.root, image=self.imageFour,relief = RAISED, bd = 0, bg = "white")
    self.boton4.configure(command = lambda: self.presionarBoton(self.imagesRoutes[3]))
    self.boton4.pack()
    self.boton4.place(anchor=CENTER, x = self.X/2+250, y = self.Y/2-100)

    self.label2 = Label(self.root, image = self.imageLevel, bd = 0, bg = "white")
    self.label2.configure()
    self.label2.pack()
    self.label2.place(anchor=CENTER, x = self.X/2, y = self.Y/2+180)
    #Aciertos acumulados
    self.label3 = Label(self.root, text = "Aciertos: ")
    self.label3.config(font=("Righteous", 20), bg = "white")
    self.label3.pack()
    self.label3.place(anchor=CENTER, x=self.X-200, y= 500)
    
    self.label4 = Label(self.root, text = "2")
    self.label4.config(font=("Righteous", 20), bg = "white")
    self.label4.pack()
    self.label4.place(anchor=CENTER, x=self.X-130, y= 500)
    #Errores Totales
    # self.label3 = Label(self.root, text = "Errores: ")
    # self.label3.config(font=("Righteous", 30), bg = "white")
    # self.label3.pack()
    # self.label3.place(anchor=CENTER, x=self.X-200, y= 550)
    
    # self.label4 = Label(self.root, text = "0")
    # self.label4.config(font=("Righteous", 30), bg = "white")
    # self.label4.pack()
    # self.label4.place(anchor=CENTER, x=self.X-90, y= 550)

    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None: 
      self.terminado = True
      self.crearResultados()
    else:
      self.pintarRonda()

  def crearResultados(self):
    segundos = self.segundos % 60
    minutos = int(self.segundos / 60)
    aciertos, fallos = self.juego.calcularResultados()
    stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos)+"\nTiempo transcurrido: "+str(minutos)+"m:"+str(segundos)+"s."
    mbox.showinfo("Juego completado", stringMBOX)
    stringResultado = "[Nivel 1] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+", Minutos: "+str(minutos)+", Segundos: "+str(segundos)+"\n"
    guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()

  def presionarBoton(self, ruta):
    self.nivelActual.validarJugada(ruta)
    if self.nivelActual.ganoNivel():
      self.pintarNivel()
    else:
      self.pintarRonda()

  def pintarRonda(self):
    self.label1.configure(text = "Nivel "+str(self.nivelActual.numNivel))
    self.label4.configure(text = self.nivelActual.contAciertos)
    carta = self.nivelActual.cargarCarta()
    self.imageLevel.configure(file = carta.ruta)
    self.label2.configure(image = self.imageLevel)

  def iniciarHilo(self):
    self.hilo2 = threading.Thread(target=self.reproducir)
    self.hilo2.start()
    
  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(1)
      self.segundos += 1
