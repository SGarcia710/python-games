from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game6.utilities import *
from game6.JuegoLaberinto import *
import os
import pygame

class VistaLaberinto: 
  # tamaño de la ventana
  X = 1200
  Y = 740
  ESPERA = 1 #cantidad de segundos de espera
  def __init__(self, parentWindow):
    self.juego = JuegoLaberinto()
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("PLANEACIÓN Y ORGANIZACIÓN")
    self.root.config(heigh=self.Y, width=self.X)
    # self.user = windll.user32
    self.root.configure(bg='white')
    self.nivelActual = None
    self.terminado = False
    self.segundos = 0
    self.movible = False
    self.root.resizable(width=False, height=False)
    # self.hilo2 = threading.Thread(target=self.ejecutarCronometro)
    # self.hilo2.start()
    self.hilo3 = threading.Thread(target=self.mouseTracking)
    self.hilo3.start()
    self.running = True
    self.ejecutandoHilo = False
    
    windowWidth = self.root.winfo_reqwidth()
    windowHeight = self.root.winfo_reqheight()

    positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
    
    self.root.geometry("+{}+{}".format(positionRight, positionDown))

    self.nivelActualStr = "Nivel 1"
    self.label1 = Label(self.root, text = self.nivelActualStr)
    self.label1.config(font=("Righteous", 30), bg = "white")
    self.label1.pack()
    self.label1.place(anchor=CENTER, x=self.X/2, y= 25)

    self.img1 = PhotoImage(file="game6/assets/images/mapa5.png")
    self.mapa = Label(self.root ,image=self.img1)
    self.mapa.pack()
    self.mapa.place(anchor=CENTER, x = self.X/2, y = self.Y/2)

    self.img2 = PhotoImage(file=self.juego.RUTA_PUNTERO)
    self.avatar = Label(self.root, image=self.img2, bd = 0, bg = "white")
    self.avatar.pack()
    self.avatar.configure(bg = "white")
    self.avatar.place(anchor=CENTER, x = self.X/2, y = self.X/2)

    self.pintarNivel()
    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None: 
      self.terminado = True
      # self.crearResultados()
    else:
      self.pintarRonda()

  def pintarRonda(self):
    self.label1.configure(text = "Nivel "+ str(self.nivelActual.numNivel+1))
    self.img1 = PhotoImage(file=self.nivelActual.rutaImagen)
    self.mapa.configure(image = self.img1)
    self.avatar.place(anchor=CENTER, x = self.nivelActual.xInicial, y = self.nivelActual.yInicial)

  def crearResultados(self):
    if self.tipoJuego == 1:
      resultadosRondas = self.juego.generarResultados()
      mbox.showinfo("Juego completado", "Visualiza los resultados en los logs.")
      stringResultado = "Fecha: "+self.fechaInicio+"\n"+resultadosRondas+"\n"
      guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()
  
  def mouseTracking(self):
    while True:
      time.sleep(.01)
      x = self.root.winfo_pointerx()
      y = self.root.winfo_pointery()
      abs_coord_x = self.root.winfo_pointerx() - self.root.winfo_rootx()
      abs_coord_y = self.root.winfo_pointery() - self.root.winfo_rooty()
      if ( 
        (abs_coord_x > self.nivelActual.xInicial-15 and abs_coord_x < self.nivelActual.xInicial+15) 
        and 
        (abs_coord_y > self.nivelActual.yInicial-15 and abs_coord_y < self.nivelActual.yInicial+15)
      ):
        self.movible = True # Si estoy dentro de las coordenadas del muñeco, pues puedo moverlo
      if self.movible:
        if ( (abs_coord_x > 192+15 and abs_coord_x < 1009-15) and (abs_coord_y > 130+15 and abs_coord_y < 610-15) ) :
          self.avatar.place(anchor= CENTER, x = abs_coord_x, y = abs_coord_y)
        if( self.nivelActual.calcularPos(abs_coord_x, abs_coord_y) ):
          self.movible = False
          self.pintarNivel()

  def ejecutarCronometro(self):
    while self.ejecutandoHilo:
      time.sleep(1)
      self.segundos += 1
