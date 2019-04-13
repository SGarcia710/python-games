from JuegoGlobos import JuegoGlobos
from tkinter import PhotoImage
from tkinter import *
import tkinter.messagebox as mbox
import time, threading
from datetime import datetime, timedelta

# mensajes = tkinter.messagebox

class VistaJuegosGlobos: 
  X = 1000
  Y = 700
  

  def __init__(self):
    self.terminado = False
    self.pausado = False
    self.fechaInicio = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.tiempoActual = 50
    hilo1 = threading.Thread(target=self.contar)
    hilo1.start()
    self.juego = JuegoGlobos()
    self.root = Tk()
    self.root.title("Control Inihibitorio")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = 1
    self.botones = []
    self.boton1 = None 
    self.boton2 = None
    self.boton3 = None
    self.boton4 = None
    self.boton5 = None
    self.boton6 = None
    self.boton7 = None
    self.boton8 = None
    self.blue = PhotoImage(file="blue.png")
    self.red = PhotoImage(file="red.png")

    windowWidth = self.root.winfo_reqwidth()
    windowHeight = self.root.winfo_reqheight()

    positionRight = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.root.winfo_screenheight()/2 - windowHeight/2)
    
    self.root.geometry("+{}+{}".format(positionRight, positionDown))
    
    self.iniciarJuego()

    self.root.mainloop()
  

  def iniciarJuego(self):
    if(self.nivelActual == 1):
      self.pintarNivel(self.juego.niveles[0])
    elif (self.nivelActual == 2):
      self.pintarNivel(self.juego.niveles[1])
    else:
      self.pintarNivel(self.juego.niveles[2])

  def pintarNivel(self, nivel):
    nivelActualStr = "Nivel "+str(self.nivelActual)
    label1 = Label(self.root, text = nivelActualStr)
    label1.config(font=("Righteous", 30), bg = "white")
    label1.pack()
    label1.place(anchor=CENTER, x=self.X/2, y= 50)
    colores = []
    for globo in nivel.globos:
      if (globo.color == globo.ROJO):
        colores.append(self.red)       
      else:
        colores.append(self.blue)
    mGlobos = nivel.globos
    self.boton1 = Button(self.root, image=colores[0], bd = 0, bg = "white")
    self.boton1.configure(command= lambda: self.accionBoton(mGlobos[0], self.boton1) )
    self.boton1.pack()
    self.boton1.place(anchor=CENTER, x = mGlobos[0].x, y = mGlobos[0].y)

    self.boton2 = Button(self.root, image=colores[1], bd = 0, bg = "white")
    self.boton2.configure(command= lambda: self.accionBoton(mGlobos[1], self.boton2) )
    self.boton2.pack()
    self.boton2.place(anchor=CENTER, x = mGlobos[1].x, y = mGlobos[1].y)

    self.boton3 = Button(self.root, image=colores[2], bd = 0, bg = "white")
    self.boton3.configure(command= lambda: self.accionBoton(mGlobos[2], self.boton3) )
    self.boton3.pack()
    self.boton3.place(anchor=CENTER, x = mGlobos[2].x, y = mGlobos[2].y)

    self.boton4 = Button(self.root, image=colores[3], bd = 0, bg = "white")
    self.boton4.configure(command= lambda: self.accionBoton(mGlobos[3], self.boton4) )
    self.boton4.pack()
    self.boton4.place(anchor=CENTER, x = mGlobos[3].x, y = mGlobos[3].y)

    self.boton5 = Button(self.root, image=colores[4], bd = 0, bg = "white")
    self.boton5.configure(command= lambda: self.accionBoton(mGlobos[4], self.boton5) )
    self.boton5.pack()
    self.boton5.place(anchor=CENTER, x = mGlobos[4].x, y = mGlobos[4].y)

    self.boton6 = Button(self.root, image=colores[5], bd = 0, bg = "white")
    self.boton6.configure(command= lambda: self.accionBoton(mGlobos[5], self.boton6) )
    self.boton6.pack()
    self.boton6.place(anchor=CENTER, x = mGlobos[5].x, y = mGlobos[5].y)

    self.boton7 = Button(self.root, image=colores[6], bd = 0, bg = "white")
    self.boton7.configure(command= lambda: self.accionBoton(mGlobos[6], self.boton7) )
    self.boton7.pack()
    self.boton7.place(anchor=CENTER, x = mGlobos[6].x, y = mGlobos[6].y)

    self.boton8 = Button(self.root, image=colores[7], bd = 0, bg = "white")
    self.boton8.configure(command= lambda: self.accionBoton(mGlobos[7], self.boton8) )
    self.boton8.pack()
    self.boton8.place(anchor=CENTER, x = mGlobos[7].x, y = mGlobos[7].y)
    

  def accionBoton(self, globo, boton):
    if(globo.color == globo.ROJO):
      self.juego.niveles[self.nivelActual-1].globosRojosPresionados += 1
    else: 
      self.juego.niveles[self.nivelActual-1].globosAzulesPresionados += 1
      
    boton.configure(state=DISABLED)
    if(self.juego.niveles[self.nivelActual-1].globosRojosPresionados == self.juego.niveles[self.nivelActual-1].numeroGlobosRojos):
      self.pausado = True
      mbox.showinfo("Felicitaciones!", "Nivel terminado.")
      self.pausado = False
      self.nivelActual += 1
      if self.nivelActual < 4:
        self.iniciarJuego()
      else:
        totalErrores = self.juego.niveles[0].globosAzulesPresionados + self.juego.niveles[1].globosAzulesPresionados + self.juego.niveles[2].globosAzulesPresionados
        totalGanados = 10
        minutos = int(self.tiempoActual/60)
        print(minutos)
        segundos = self.tiempoActual%60
        print(segundos)
        string = "Total aciertos: "+str(totalGanados)+". \nTotal Errores: "+str(totalErrores)+"\nTiempo transcurrido: "+str(minutos)+"m:"+str(segundos)+"s."
        self.terminado = True
        mbox.showinfo("Juego completado", string)
        print("Nivel acabado")
        self.root.destroy()

  def contar(self):
    while not self.terminado:
      if not self.pausado:
        print(self.tiempoActual)
        time.sleep(1)
        self.tiempoActual += 1