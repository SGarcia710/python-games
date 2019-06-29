from game5.JuegoRana import *
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from tkinter import PhotoImage
from datetime import datetime, timedelta
from game5.utilities import *
import os

class Vista: 
  # tamaño de la ventana
  X = 800
  Y = 740
  ESPERA = 1 #cantidad de segundos de espera
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
    self.label1.place(anchor=CENTER, x=self.X/2, y= 25)

    #nenufares
    self.hojaImage = PhotoImage(file=self.juego.RUTA_HOJA)
    self.arregloBotones = []

    self.boton1 = Button(self.root, image=self.hojaImage,relief = RAISED,  bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[0][0]))
    self.boton1.pack()
    self.boton1.place(anchor=CENTER, x = 200, y = 190)
    self.arregloBotones.append(self.boton1)
    self.boton2 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[0][1]))
    self.boton2.pack()
    self.boton2.place(anchor=CENTER, x = 300, y = 190)
    self.arregloBotones.append(self.boton2)
    self.boton3 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[0][2]))
    self.boton3.pack()
    self.boton3.place(anchor=CENTER, x = 400, y = 190)
    self.arregloBotones.append(self.boton3)
    self.boton4 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[0][3]))
    self.boton4.pack()
    self.boton4.place(anchor=CENTER, x = 500, y = 190) 
    self.arregloBotones.append(self.boton4)
    self.boton5 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[0][4]))
    self.boton5.pack()
    self.boton5.place(anchor=CENTER, x = 600, y = 190) 
    self.arregloBotones.append(self.boton5)
    self.boton6 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[1][0]))
    self.boton6.pack()
    self.boton6.place(anchor=CENTER, x = 200, y = 280) 
    self.arregloBotones.append(self.boton6)
    self.boton7 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[1][1]))
    self.boton7.pack()
    self.boton7.place(anchor=CENTER, x = 300, y = 280) 
    self.arregloBotones.append(self.boton7)
    self.boton8 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[1][2]))
    self.boton8.pack()
    self.boton8.place(anchor=CENTER, x = 400, y = 280) 
    self.arregloBotones.append(self.boton8)
    self.boton9 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[1][3]))
    self.boton9.pack()
    self.boton9.place(anchor=CENTER, x = 500, y = 280) 
    self.arregloBotones.append(self.boton9)
    self.boton10 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[1][4]))
    self.boton10.pack()
    self.boton10.place(anchor=CENTER, x = 600, y = 280) 
    self.arregloBotones.append(self.boton10)
    self.boton11 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[2][0]))
    self.boton11.pack()
    self.boton11.place(anchor=CENTER, x = 200, y = 370) 
    self.arregloBotones.append(self.boton11)
    self.boton12 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[2][1]))
    self.boton12.pack()
    self.boton12.place(anchor=CENTER, x = 300, y = 370) 
    self.arregloBotones.append(self.boton12)
    self.boton13 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[2][2]))
    self.boton13.pack()
    self.boton13.place(anchor=CENTER, x = 400, y = 370) 
    self.arregloBotones.append(self.boton13)
    self.boton14 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[2][3]))
    self.boton14.pack()
    self.boton14.place(anchor=CENTER, x = 500, y = 370) 
    self.arregloBotones.append(self.boton14)
    self.boton15 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[2][4]))
    self.boton15.pack()
    self.boton15.place(anchor=CENTER, x = 600, y = 370) 
    self.arregloBotones.append(self.boton15)
    self.boton16 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[3][0]))
    self.boton16.pack()
    self.boton16.place(anchor=CENTER, x = 200, y = 460) 
    self.arregloBotones.append(self.boton16)
    self.boton17 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[3][1]))
    self.boton17.pack()
    self.boton17.place(anchor=CENTER, x = 300, y = 460) 
    self.arregloBotones.append(self.boton17)
    self.boton18 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[3][2]))
    self.boton18.pack()
    self.boton18.place(anchor=CENTER, x = 400, y = 460) 
    self.arregloBotones.append(self.boton18)
    self.boton19 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[3][3]))
    self.boton19.pack()
    self.boton19.place(anchor=CENTER, x = 500, y = 460) 
    self.arregloBotones.append(self.boton19)
    self.boton20 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[3][4]))
    self.boton20.pack()
    self.boton20.place(anchor=CENTER, x = 600, y = 460) 
    self.arregloBotones.append(self.boton20)
    self.boton21 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[4][0]))
    self.boton21.pack()
    self.boton21.place(anchor=CENTER, x = 200, y = 550) 
    self.arregloBotones.append(self.boton21)
    self.boton22 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[4][1]))
    self.boton22.pack()
    self.boton22.place(anchor=CENTER, x = 300, y = 550) 
    self.arregloBotones.append(self.boton22)
    self.boton23 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[4][2]))
    self.boton23.pack()
    self.boton23.place(anchor=CENTER, x = 400, y = 550) 
    self.arregloBotones.append(self.boton23)
    self.boton24 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[4][3]))
    self.boton24.pack()
    self.boton24.place(anchor=CENTER, x = 500, y = 550) 
    self.arregloBotones.append(self.boton24)
    self.boton25 = Button(self.root, image=self.hojaImage,relief = RAISED, bd = 0, bg = "white", command = lambda: self.presionarBoton(self.juego.hojas[4][4]))
    self.boton25.pack()
    self.boton25.place(anchor=CENTER, x = 600, y = 550) 
    self.arregloBotones.append(self.boton25)
    #Ranas
    self.ranaImage = None
    self.ranaOverImage = None
    self.rana = Label(self.root, bd = 0, bg = "white")
    # self.root.wm_attributes('-transparentcolor', self.root['bg'])
    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None: 
      self.terminado = True
      self.crearResultados()
    else:
      self.pintarRonda()

  def presionarBoton(self, hoja):
    self.pintarNivel()
  
  def pintarRonda(self):
    self.label1.configure(text = "Nivel "+ str(self.nivelActual.numNivel+1))
    if self.nivelActual.tipoNivel == self.nivelActual.TIPO_NIVEL_PROGRESIVO:
      self.ranaImage = PhotoImage(file=self.juego.RUTA_RANA)
      self.ranaOverImage = PhotoImage(file = "game5/assets/renders/RanaOverNenufar.png")
      self.rana.configure(image = self.ranaImage)
      self.rana.pack()
      self.rana.place(anchor=CENTER, x = self.X/2, y = 90) 
    else:
      self.ranaImage = PhotoImage(file=self.juego.RUTA_RANA_INV)
      self.ranaOverImage = PhotoImage(file = "game5/assets/renders/RanaOverNenufarInv.png")
      self.rana.configure(image = self.ranaImage)
      self.rana.pack()
      self.rana.place(anchor=CENTER, x = self.X/2, y = 660)
    self.root.after(1000, self.pintarMovimientos) 

  def pintarMovimientos(self):
    movimiento = self.nivelActual.obtenerMovimiento()
    if movimiento:
      self.rana.configure(image = self.ranaOverImage)
      self.rana.place(anchor= CENTER, x = movimiento.y, y = movimiento.x)
      self.root.after(1000, self.pintarMovimientos)
    else:
      self.rana.configure(image = self.ranaImage)
      if self.nivelActual.tipoNivel == self.nivelActual.TIPO_NIVEL_PROGRESIVO:
        self.rana.place(anchor=CENTER, x = self.X/2, y = 660)
      else:
        self.rana.place(anchor=CENTER, x = self.X/2, y = 90)
    



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
