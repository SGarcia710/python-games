from utilities import *

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
    self.numeroGlobo = 0
    self.generarGlobos()

  def imprimirDatos(self):
    for globo in self.globos:
      print(globo.color, " ", globo.x, " ", globo.y,".")

  def generarGlobos(self):
    i = 1
    for globo in range(self.numeroGlobos): 
      if(i <= self.numeroGlobosRojos):
        self.globos.append(Globo(Globo.ROJO))
        i+=1
      else:
        self.globos.append(Globo(Globo.AZUL))
    desordenarLista(self.globos)
    XT = 200
    x = XT
    YT = 200
    y = YT
    i = 1
    for globo in self.globos:
      globo.setX(x)
      globo.setY(y)
      x += 200
      i += 1
      if i == (self.numeroGlobos/2)+1:
        x = XT
        y = YT + 250


class Globo:
  ROJO = "rojo"
  AZUL = "azul"
  def __init__(self, color):
    self.color = color
    self.x = 0
    self.y = 0
    self.presionado = False
   
  def setX(self, x):
    self.x = x
  
  def setY(self, y):
    self.y = y
  
  def desactivar(self):
    self.presionado = True

