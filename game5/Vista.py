from game5.JuegoRana import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game5.utilities import *
import os
from pygame import mixer
from tinytag import TinyTag
import math

class Vista: 
  # tamaño de la ventana
  X = 1000
  Y = 700
  def __init__(self, parentWindow, tipoJuego):
    self.juego = JuegoRana(tipoJuego)
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("MEM. TRAB. BIOESPACIAL.")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None
    self.terminado = False
    self.segundos = 0
    self.root.resizable(width=False, height=False)
    # self.hilo2 = threading.Thread(target=self.ejecutarCronometro)
    # self.hilo2.start()
    
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

    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    for fila in self.juego.hojas:
      for columna in fila:
        
  # def crearResultados(self):
  #   segundos = self.segundos % 60
  #   minutos = int(self.segundos / 60)
  #   aciertos, fallos = self.juego.calcularResultados()
  #   stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos)+"\nTiempo transcurrido: "+str(minutos)+"m:"+str(segundos)+"s."
  #   mbox.showinfo("Juego completado", stringMBOX)
  #   stringResultado = "[Nivel 1] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+", Minutos: "+str(minutos)+", Segundos: "+str(segundos)+"\n"
  #   guardarLog(stringResultado)
  #   self.root.destroy()
  #   self.parentWindow.deiconify()

  # def presionarBoton(self, ruta):

  # def iniciarHilo(self):
  #   self.hilo2 = threading.Thread(target=self.reproducir)
  #   self.hilo2.start()
    
  # def ejecutarCronometro(self):
  #   while(not self.terminado):
  #     time.sleep(1)
  #     self.segundos += 1
