from game1.utilities import *

class JuegoGlobos:
  NUMERO_NIVELES_TOTAL = 20 
  NUMERO_NIVELES_ROJOS = int(NUMERO_NIVELES_TOTAL * 0.80)
  NUMERO_NIVELES_TRAMPA = int(NUMERO_NIVELES_TOTAL * 0.20)
  GLOBOS_ROJOS_NIVELES = []
  NUMERO_GLOBOS = 8
  
  def __init__(self):
    self.niveles = []
    self.nivelActual = 0
    self.generarNiveles()
  
  def generarNiveles(self):
    for i in range(self.NUMERO_NIVELES_ROJOS):
      self.niveles.append(Nivel(numeroAleatorio(1,self.NUMERO_GLOBOS), self.NUMERO_GLOBOS))
    for i in range(self.NUMERO_NIVELES_TRAMPA):
      self.niveles.append(Nivel(0, self.NUMERO_GLOBOS))
    desordenarLista(self.niveles)

  def obtenerNivel(self):
    if self.nivelActual < len(self.niveles):
      nivel = self.niveles[self.nivelActual]
      self.nivelActual += 1
      return nivel
    else:
      return None
  
  def calcularResultados(self):
    aciertos = 0
    errores = 0
    for nivel in self.niveles:
      if (nivel.numeroGlobosRojos > 0 and nivel.presionado) or (nivel.numeroGlobosRojos == 0 and not nivel.presionado):
        aciertos += 1
      else:
        errores += 1
    return aciertos, errores

class Nivel:
  def __init__(self, numeroGlobosRojos, numeroGlobos):
    self.globos = []
    self.numeroGlobos = numeroGlobos
    self.numeroGlobosRojos = numeroGlobosRojos
    self.presionado = False
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

  def presionarBotonGo(self):
    self.presionado = True

class Globo:
  ROJO = "rojo"
  AZUL = "azul"
  RUTA_AZUL = "game1/assets/blue.png"
  RUTA_ROJO = "game1/assets/red.png"
  def __init__(self, color):
    self.ruta = self.RUTA_AZUL
    if color == self.ROJO:
      self.ruta = self.RUTA_ROJO