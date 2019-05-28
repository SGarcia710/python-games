from game4.JuegoCartas import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game4.utilities import *
from game4.assets.configs.config import *
import os
from pygame import mixer
from tinytag import TinyTag
import math

class VistaCartas: 
  # tamaño de la ventana
  X = 1000 
  Y = 700
  def __init__(self, parentWindow):
    mixer.init()
    self.juego = JuegoCartas()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("MEM. T. FONOLÓGICA.")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None
    self.segundos = 0
    self.terminado2 = False
    self.root.resizable(width=False, height=False)
    #self.hilo3 = threading.Thread(target=self.ejecutarCronometro)
    #self.hilo3.start()
    # self.hilo2 = None
    self.imageOneStr = "game4/assets/images/triangulo,rojo,1.png"
    self.imageTwoStr = "game4/assets/images/estrella,verde,2.png"
    self.imageThreeStr = "game4/assets/images/cruz,amarillo,3.png"
    self.imageFourStr = "game4/assets/images/circulo,azul,4.png"
    self.imageOne = PhotoImage(file=imageOneStr)
    self.imageTwo = PhotoImage(file=imageTwoStr)
    self.imageThree = PhotoImage(file=imageThreeStr)
    self.imageFour = PhotoImage(file=imageFourStr)

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
    self.boton1.configure(command = lambda: self.presionarBoton(self.imageOneStr))
    self.boton1.pack()
    self.boton1.place(anchor=CENTER, x = self.X/2-250, y = self.Y/2-100)
    self.boton2 = Button(self.root, image=self.imageTwo,relief = RAISED, bd = 0, bg = "white")
    self.boton2.configure(command = lambda: self.presionarBoton(self.imageTwoStr))
    self.boton2.pack()
    self.boton2.place(anchor=CENTER, x = self.X/2-85, y = self.Y/2-100)
    self.boton3 = Button(self.root, image=self.imageThree,relief = RAISED, bd = 0, bg = "white")
    self.boton3.configure(command = lambda: self.presionarBoton(self.imageThreeStr))
    self.boton3.pack()
    self.boton3.place(anchor=CENTER, x = self.X/2+85, y = self.Y/2-100)
    self.boton4 = Button(self.root, image=self.imageFour,relief = RAISED, bd = 0, bg = "white")
    self.boton4.configure(command = lambda: self.presionarBoton(self.imageFourStr))
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

    # self.pintarNivel()

    self.root.mainloop()

  def presionarBoton(self, ruta):
    self.nivelActual.validarOpcion(ruta)

  def iniciarHilo(self):
    self.hilo2 = threading.Thread(target=self.reproducir)
    self.hilo2.start()
    
  def ejecutarCronometro(self):
    while(not self.terminado2):
      time.sleep(1)
      self.segundos += 1
