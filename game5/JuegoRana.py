from game5.utilities import *

class JuegoRana:
  RUTA_RANA = ""
  RUTA_HOJA = ""
  NUM_SECUENCIAS_NIVEL = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  NUM_SECUENCIAS_NIVEL_PRUEBA = [5,7,8,9,10]
  NUM_HOJAS = 5
  def __init__(self):
    self.nivelesPrueba = None
    self.niveles = None
    self.hojas = None
    self.cargarHojas()
    self.cargarNivelesPrueba()
    self.cargarNiveles()

  def cargarHojas(self):
    x, y = 0, 0
    for hojax in range(self.NUM_HOJAS):
      y = 0
      for hojay in range(self.NUM_HOJAS):
        self.hojas.append(Hoja(x,y))
        y += 1
      x += 1

  def cargarNivelesPrueba(self):
    index = 1
    for secuencia in self.NUM_SECUENCIAS_NIVEL_PRUEBA:
      camino = []
      while len(camino) < secuencia:
        indice = numeroAleatorio(0,len(self.hojas)-1)
        hoja = self.hojas[indice]
        if hoja not in camino:
          camino.append(hoja)
      self.nivelesPrueba.append(index, camino)
      index += 1
    for nivelPrueba in nivelesPrueba:
      nuevoCamino = nivelPrueba.camino
      nuevoCamino.reverse()
      self.nivelesPrueba.append(index, nuevoCamino)
      index += 1

  def cargarNiveles(self):
    index = 1
    for secuencia in self.NUM_SECUENCIAS_NIVEL:
      camino = []
      while len(camino) < secuencia:
        indice = numeroAleatorio(0,len(self.hojas)-1)
        hoja = self.hojas[indice]
        if hoja not in camino:
          camino.append(hoja)
      self.niveles.append(index, camino)
      index += 1
    for nivelPrueba in niveles:
      nuevoCamino = nivelPrueba.camino
      nuevoCamino.reverse()
      self.niveles.append(index, nuevoCamino)
      index += 1

class Nivel:
  def __init__(self, numNivel, camino):
    self.numNivel = numNivel
    self.numPaso = 0
    self.segundos = 0
    self.aciertos = 0
    self.errores = 0
    self.camino = camino

class Hoja:
  def __init__(self, x, y):
    self.x = x
    self.y = y