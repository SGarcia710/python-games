from JuegoGlobos import JuegoGlobos
from tkinter import PhotoImage
from tkinter import *

class VistaJuegosGlobos: 
  X = 1000
  Y = 700

  


  def __init__(self): 
    self.juego = JuegoGlobos()
    self.root = Tk()
    self.root.title("Nivel 1")
    self.root.config(heigh=self.Y, width=self.X)
    self.root.configure(bg='white')
    self.nivelActual = 1
    self.botones = []
    self.boton1 = None 
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
    for globo in nivel.globos:
      if (globo.color == globo.ROJO):
        image = self.red
      else:
        image = self.blue 
      boton = Button(self.root, text="asdfasdf", image=image, bd = 0, bg = "white")
      boton.configure(command= lambda: boton.configure(state = DISABLED) )
      boton.pack()
      boton.place(anchor=CENTER, x = globo.x, y = globo.y)
      self.botones.append(boton)

  # def accionBoton(self):
    
  # def callback_factory(self, boton):
  #   return lambda: button["state"] = DISABLED