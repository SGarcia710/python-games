from game4.JuegoNumeros import *
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

class VistaNumeros: 
  # tamaño de la ventana
  X = 1000 
  Y = 700
  BANANA = "#e55039"
  TEXT_FONT = 70
  BTNSIZEH = 85
  BTNSIZEW = 122
  def __init__(self, parentWindow):
    self.juego = JuegoNumeros()
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
    windowWidth = self.root.winfo_reqwidth()
    windowHeight = self.root.winfo_reqheight()

    positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
    
    self.root.geometry("+{}+{}".format(positionRight, positionDown))
    self.nivelActualStr = "Nivel"
    self.label1 = Label(self.root, text = self.nivelActualStr)
    self.label1.config(font=("Righteous", 30), bg = "white")
    self.label1.pack()
    self.label1.place(anchor=CENTER, x=(self.X/2), y= 50)

    self.cuadro1 = Label(self.root, text= "_")
    self.cuadro1.config(font=("Righteous", self.TEXT_FONT), bg = "white")    
    self.cuadro1.pack()
    self.cuadro1.place(anchor=CENTER, x = (self.X/2)-200, y = 200)
    self.cuadro2 = Label(self.root, text= "?")
    self.cuadro2.config(font=("Righteous", self.TEXT_FONT), bg = "white")    
    self.cuadro2.pack()
    self.cuadro2.place(anchor=CENTER, x = (self.X/2)-100, y = 200)
    self.cuadro3 = Label(self.root, text= "_")
    self.cuadro3.config(font=("Righteous", self.TEXT_FONT), bg = "white")    
    self.cuadro3.pack()
    self.cuadro3.place(anchor=CENTER, x = (self.X/2), y = 200)
    self.cuadro4 = Label(self.root, text= "=")
    self.cuadro4.config(font=("Righteous", self.TEXT_FONT), bg = "white")    
    self.cuadro4.pack()
    self.cuadro4.place(anchor=CENTER, x = (self.X/2)+100, y = 200)
    self.cuadro5 = Label(self.root, text= "_")
    self.cuadro5.config(font=("Righteous", self.TEXT_FONT), bg = "white")    
    self.cuadro5.pack()
    self.cuadro5.place(anchor=CENTER, x = (self.X/2)+ 200, y = 200)
    
    self.numeroBoton1 = 1
    self.numeroBoton2 = 2
    self.numeroBoton3 = 3
    self.numeroBoton4 = 4
    self.boton1 = Button(self.root, text = self.numeroBoton1, bg = self.BANANA, fg = "white", relief = GROOVE)
    self.boton1.configure(font=("Righteous", self.TEXT_FONT), command = lambda: self.presionarBoton(self.numeroBoton1))
    self.boton1.pack()
    self.boton1.place(anchor=CENTER, x = self.X/2-250, y = 500, height = self.BTNSIZEH, width = self.BTNSIZEW)
    self.boton2 = Button(self.root, text = self.numeroBoton1, bg = self.BANANA, fg = "white", relief = GROOVE)
    self.boton2.configure(font=("Righteous", self.TEXT_FONT), command = lambda: self.presionarBoton(self.numeroBoton2))
    self.boton2.pack()
    self.boton2.place(anchor=CENTER, x = self.X/2-85, y = 500, height = self.BTNSIZEH, width = self.BTNSIZEW)
    self.boton3 = Button(self.root, text = self.numeroBoton1, bg = self.BANANA, fg = "white", relief = GROOVE)
    self.boton3.configure(font=("Righteous", self.TEXT_FONT), command = lambda: self.presionarBoton(self.numeroBoton3))
    self.boton3.pack()
    self.boton3.place(anchor=CENTER, x = self.X/2+85, y = 500, height = self.BTNSIZEH, width = self.BTNSIZEW)
    self.boton4 = Button(self.root, text = self.numeroBoton1, bg = self.BANANA, fg = "white", relief = GROOVE)
    self.boton4.configure(font=("Righteous", self.TEXT_FONT), command = lambda: self.presionarBoton(self.numeroBoton4))
    self.boton4.pack()
    self.boton4.place(anchor=CENTER, x = self.X/2+250, y = 500, height = self.BTNSIZEH, width = self.BTNSIZEW)

    #Aciertos acumulados
    self.label3 = Label(self.root, text = "Aciertos: ")
    self.label3.config(font=("Righteous", 20), bg = "white")
    self.label3.pack()
    self.label3.place(anchor=CENTER, x=self.X-200, y= self.Y-100)
    
    self.label4 = Label(self.root, text = "2")
    self.label4.config(font=("Righteous", 20), bg = "white")
    self.label4.pack()
    self.label4.place(anchor=CENTER, x=self.X-130, y= self.Y-100)
    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None: 
      self.terminado = True
      self.crearResultados()
    else:
      self.pintarRonda()

  def presionarBoton(self,numero):
    self.nivelActual.presionarBoton(numero)
    if self.nivelActual.botonesPresionados():
      self.nivelActual.validarRonda()
      if self.nivelActual.ganoNivel():
        self.pintarNivel()
      else:
        self.pintarRonda()
    else:
      self.pintarOperacion()

  def pintarRonda(self):
    self.label1.configure(text = "Nivel "+str(self.juego.nivelActual))
    self.label4.configure(text = self.nivelActual.contAciertos)
    self.numeroBoton1 = self.nivelActual.operacion.listaNumeros[0]
    self.numeroBoton2 = self.nivelActual.operacion.listaNumeros[1]
    self.numeroBoton3 = self.nivelActual.operacion.listaNumeros[2]
    self.numeroBoton4 = self.nivelActual.operacion.listaNumeros[3]
    self.boton1.configure(text = self.numeroBoton1)
    self.boton2.configure(text = self.numeroBoton2)
    self.boton3.configure(text = self.numeroBoton3)
    self.boton4.configure(text = self.numeroBoton4)

    self.pintarOperacion()
  

  def pintarOperacion(self):
    temp = self.nivelActual.operacion.numerosUsuario
    self.cuadro1.configure(text = "_" if temp[0] is -1 else temp[0] )
    self.cuadro3.configure(text = "_" if temp[1] is -1 else temp[1] )
    self.cuadro5.configure(text = "_" if temp[2] is -1 else temp[2] )

  def crearResultados(self):
    segundos = self.segundos % 60
    minutos = int(self.segundos / 60)
    aciertos, fallos = self.juego.calcularResultados()
    stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos)+"\nTiempo transcurrido: "+str(minutos)+"m:"+str(segundos)+"s."
    mbox.showinfo("Juego completado", stringMBOX)
    stringResultado = "[Nivel 2] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+", Minutos: "+str(minutos)+", Segundos: "+str(segundos)+"\n"
    guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()

  def iniciarHilo(self):
    self.hilo2 = threading.Thread(target=self.reproducir)
    self.hilo2.start()
    
  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(1)
      self.segundos += 1
