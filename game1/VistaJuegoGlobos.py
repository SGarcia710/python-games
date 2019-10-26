from game1.JuegoGlobos import JuegoGlobos
from tkinter import PhotoImage
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from datetime import datetime, timedelta
from game1.utilities import *
from game1.ControlInhibitorio import *

class VistaJuegoGlobos: 
  # tamaño de la ventana
  X = 1000
  Y = 710
  TIEMPO_RESP = 3 # 3000ms
  def __init__(self, parentWindow):
    self.juego = JuegoGlobos()
    print(str(len(self.juego.niveles)))
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.root = Toplevel()
    self.parentWindow = parentWindow
    self.root.title("Control Inhibitorio")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = None #Objeto de tipo nivel
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

    self.img1 = PhotoImage(file="game1/assets/blue.png")
    self.img2 = PhotoImage(file="game1/assets/blue.png")
    self.img3 = PhotoImage(file="game1/assets/blue.png")
    self.img4 = PhotoImage(file="game1/assets/blue.png")
    self.img5 = PhotoImage(file="game1/assets/blue.png")
    self.img6 = PhotoImage(file="game1/assets/blue.png")
    self.img7 = PhotoImage(file="game1/assets/blue.png")
    self.img8 = PhotoImage(file="game1/assets/blue.png")

    self.cuadro1 = Label(self.root, image=self.img1, bg = "white")
    self.cuadro1.pack()
    self.cuadro1.place(anchor=CENTER, x = (self.X/2)-225, y = 200)
    self.cuadro2 = Label(self.root, image=self.img2, bg = "white")
    self.cuadro2.pack()
    self.cuadro2.place(anchor=CENTER, x = (self.X/2)-75, y = 200)
    self.cuadro3 = Label(self.root, image=self.img3, bg = "white")
    self.cuadro3.pack()
    self.cuadro3.place(anchor=CENTER, x = (self.X/2)+75, y = 200)
    self.cuadro4 = Label(self.root, image=self.img4, bg = "white")
    self.cuadro4.pack()
    self.cuadro4.place(anchor=CENTER, x = (self.X/2)+225, y = 200)
    self.cuadro5 = Label(self.root, image=self.img5, bg = "white")
    self.cuadro5.pack()
    self.cuadro5.place(anchor=CENTER, x = (self.X/2)-225, y = 450)
    self.cuadro6 = Label(self.root, image=self.img6, bg = "white")
    self.cuadro6.pack()
    self.cuadro6.place(anchor=CENTER, x = (self.X/2)-75, y = 450)
    self.cuadro7 = Label(self.root, image=self.img7, bg = "white")
    self.cuadro7.pack()
    self.cuadro7.place(anchor=CENTER, x = (self.X/2)+75, y = 450)
    self.cuadro8 = Label(self.root, image=self.img8, bg = "white")
    self.cuadro8.pack()
    self.cuadro8.place(anchor=CENTER, x = (self.X/2)+225, y = 450)

    self.botonGo = Button(self.root, text = "Go", bd = 1, relief = GROOVE, bg = BLUE , fg = "white", font=("Arial", 16),command= self.accionBoton)
    self.botonGo.pack()
    self.botonGo.place(anchor=CENTER, x = self.X/2, y = 620, width = 150, heigh = 50)
    
    self.pintarNivel()

    self.root.mainloop()

  def pintarNivel(self):
    self.nivelActual = self.juego.obtenerNivel()
    if self.nivelActual is None:
      self.terminado = True
      self.crearResultados()
    else:
      self.label1.configure(text="Nivel " + str(self.juego.nivelActual))
      self.img1.configure(file = self.nivelActual.globos[0].ruta)
      self.img2.configure(file = self.nivelActual.globos[1].ruta)
      self.img3.configure(file = self.nivelActual.globos[2].ruta)
      self.img4.configure(file = self.nivelActual.globos[3].ruta)
      self.img5.configure(file = self.nivelActual.globos[4].ruta)
      self.img6.configure(file = self.nivelActual.globos[5].ruta)
      self.img7.configure(file = self.nivelActual.globos[6].ruta)
      self.img8.configure(file = self.nivelActual.globos[7].ruta)

      self.cuadro1.configure(image = self.img1)
      self.cuadro2.configure(image = self.img2)
      self.cuadro3.configure(image = self.img3)
      self.cuadro4.configure(image = self.img4)
      self.cuadro5.configure(image = self.img5)
      self.cuadro6.configure(image = self.img6)
      self.cuadro7.configure(image = self.img7)
      self.cuadro8.configure(image = self.img8)
  
  def crearResultados(self):
    aciertos, fallos = self.juego.calcularResultados()
    stringMBOX = "Total aciertos: "+str(aciertos)+". \nTotal Errores: "+str(fallos) + "."
    mbox.showinfo("Juego completado", stringMBOX)
    stringResultado = "[Nivel 1] Fecha: "+self.fechaInicio+", Aciertos: "+str(aciertos)+", Errores: "+str(fallos)+"\n"
    guardarLog(stringResultado)
    self.root.destroy()
    self.parentWindow.deiconify()

  def accionBoton(self):
    self.nivelActual.presionarBotonGo()
    self.reiniciar()

  def reiniciar(self):
    self.segundos = 0
    self.pintarNivel()
    
  def ejecutarCronometro(self):
    while(not self.terminado):
      time.sleep(0.1)
      self.segundos += 0.1
      if self.segundos >= self.TIEMPO_RESP:
        self.reiniciar()