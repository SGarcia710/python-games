from game2.JuegoProcesamiento import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game2.utilities import *
import time, threading
import os

class VistaJuegoVelPro: 
  # tamaño de la ventana
  X = 1280
  Y = 710
  def __init__(self, parentWindow, tipo):
    self.juego = VelocidadProcesamiento(tipo)
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("Velocidad Procesamiento")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None
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
    self.nivelActualStr = "Nivel "
    self.label1 = Label(self.root, text = self.nivelActualStr)
    self.label1.config(font=("Righteous", 30), bg = "white")
    self.label1.pack()
    self.label1.place(anchor=CENTER, x=self.X/2, y= 50)

    self.img1 = PhotoImage(file="game2/assets/images/Avion.png")
    self.img2 = PhotoImage(file="game2/assets/images/Avion.png")
    self.img3 = PhotoImage(file="game2/assets/images/Avion.png")

    self.cuadro1 = Label(self.root, image=self.img1)
    self.cuadro1.pack()
    self.cuadro1.place(anchor=CENTER, x = (self.X/2)-420, y = 250)
    self.cuadro2 = Label(self.root, image=self.img2)
    self.cuadro2.pack()
    self.cuadro2.place(anchor=CENTER, x = self.X/2, y = 250)
    self.cuadro3 = Label(self.root, image=self.img3)
    self.cuadro3.pack()
    self.cuadro3.place(anchor=CENTER, x = (self.X/2)+420, y = 250)
    
    self.cuadroOpcion = None

    if self.juego.tipoJuego == VelocidadProcesamiento.JUEGO_UNO: 
      self.imgOpcion = PhotoImage(file="game2/assets/icons/Avion.png")
      self.smaller_image = self.imgOpcion.subsample(2, 2) #Resize del objeto PhotoImage
      self.cuadroOpcion = Label(self.root, image = self.smaller_image )
    else:
      self.txtOpcion = "_"
      self.cuadroOpcion = Label(self.root, text = self.txtOpcion, font=("Righteous", 50))
    self.cuadroOpcion.configure(bg = "white")
    self.cuadroOpcion.pack()
    self.cuadroOpcion.place(anchor=CENTER, x = self.X/2, y = 445)

    self.botonZ = Button(self.root, text = "Z", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 16),command= lambda: self.accionBoton(1))
    self.botonZ.pack()
    self.botonZ.place(anchor=CENTER, x = 300, y = self.Y-150, width = 150, heigh = 50)

    self.botonG = Button(self.root, text = "-", bd = 1, relief = GROOVE, bg = BLUE, fg = "white", font=("Arial", 16),command= lambda: self.accionBoton(2))
    self.botonG.pack()
    self.botonG.place(anchor=CENTER, x = self.X-300, y = self.Y-150, width = 150, heigh = 50)

    self.pintarNivel()

    self.root.mainloop()

  def accionBoton(self, tBoton):
    if tBoton == 1:
      self.nivelActual.resultado = self.nivelActual.RES_SI
    else:
      self.nivelActual.resultado = self.nivelActual.RES_NO
    self.pintarNivel()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None:
      self.terminado = True
      self.crearResultados()
    else:
      #self.hack() #Trampa
      self.label1.configure(text="Nivel " + str(self.nivelActual.numNivel + 1))
      self.img1.configure(file = self.nivelActual.ilustraciones[0].ruta)
      self.img2.configure(file = self.nivelActual.ilustraciones[1].ruta)
      self.img3.configure(file = self.nivelActual.ilustraciones[2].ruta)

      self.cuadro1.configure(image = self.img1)
      self.cuadro2.configure(image = self.img2)
      self.cuadro3.configure(image = self.img3)

      if self.juego.tipoJuego == VelocidadProcesamiento.JUEGO_UNO:
        self.imgOpcion.configure(file = self.nivelActual.icono.ruta)
        self.smaller_image = self.imgOpcion.subsample(2, 2) #Resize del objeto PhotoImage
        self.cuadroOpcion.configure(image = self.smaller_image)
      else:
        self.cuadroOpcion.configure(text = self.nivelActual.icono.palabra[0])
      
      
  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(1)
      self.segundos += 1

  def crearResultados(self):
    segundos = self.segundos % 60
    minutos = int(self.segundos / 60)
    aciertos, fallos = self.juego.calcularResultados()
    stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos)+"\nTiempo transcurrido: "+str(minutos)+"m:"+str(segundos)+"s."
    mbox.showinfo("Juego completado", stringMBOX)
    stringResultado = "[Nivel "+ str(self.juego.tipoJuego) +"] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+", Minutos: "+str(minutos)+", Segundos: "+str(segundos)+"\n"
    guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()

  def hack(self):
    os.system('cls')
    print(str(self.nivelActual.ilustraciones[0].palabras) + " " + str(self.nivelActual.ilustraciones[1].palabras) + " " + str(self.nivelActual.ilustraciones[2].palabras) + " ======== " + self.nivelActual.icono.palabra)