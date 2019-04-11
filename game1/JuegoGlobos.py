from utilities import *
from tkinter import *

class JuegoGlobos: 
  NUMERO_NIVELES = 3
  GLOBOS_ROJOS_NIVEL_1 = 5
  GLOBOS_ROJOS_NIVEL_2 = 1
  GLOBOS_ROJOS_NIVEL_3 = 4
  NUMERO_GLOBOS = 8
  
  def __init__(self):
    self.niveles = []
    self.generarNiveles()
  
  def generarNiveles(self):
    self.niveles.append(Nivel(self.GLOBOS_ROJOS_NIVEL_1, self.NUMERO_GLOBOS))
    self.niveles.append(Nivel(self.GLOBOS_ROJOS_NIVEL_2, self.NUMERO_GLOBOS))
    self.niveles.append(Nivel(self.GLOBOS_ROJOS_NIVEL_3, self.NUMERO_GLOBOS))


class Nivel:
  def __init__(self, numeroGlobosRojos, numeroGlobos):
    self.numeroGlobos = numeroGlobos
    self.numeroGlobosRojos = numeroGlobosRojos
    self.globos = []
    self.generarGlobos()

  def generarGlobos(self):
    i = 1
    for globo in range(self.numeroGlobos): 
      if(i <= self.numeroGlobosRojos):
        self.globos.append(Globo(Globo.ROJO))
        i+=1
      else:
        self.globos.append(Globo(Globo.AZUL))
    desordenarLista(self.globos)
    x = 100
    y = 100
    i = 1
    for globo in self.globos:
      globo.setX(x)
      globo.setY(y)
      x += 150
      i += 1
      if i == self.numeroGlobos/2:
        x = 100
        y = 300


class Globo:
  GLOBO_ROJO_IMAGEN = "assets/red.png"
  GLOBO_AZUL_IMAGEN = "assets/blue.png"
  ROJO = "rojo"
  AZUL = "azul"
  def __init__(self, color):
    self.color = color
    self.x = 0
    self.y = 0
    self.presionado = False
    if (color == self.ROJO):
      self.rutaGlobo = self.GLOBO_ROJO_IMAGEN
    else:
      self.rutaGlobo = self.GLOBO_AZUL_IMAGEN
    
  def setX(self, x):
    self.x = x
  
  def setY(self, y):
    self.y = y

  def sayHello(self):
    print("hello")
  



  def desactivar(self):
    self.presionado = True

