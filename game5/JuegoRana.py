from game5.utilities import *

class JuegoRana:
  RUTA_RANA = "game5/assets/renders/RanaP.png"
  RUTA_RANA_INV = "game5/assets/renders/RanaPInvertida.png"
  RUTA_HOJA = "game5/assets/renders/NenufarP.png"
  NUM_SECUENCIAS_NIVEL = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  NUM_SECUENCIAS_NIVEL_PRUEBA = [5,7,8,9,10]
  NUM_HOJAS = 5
  def __init__(self, tipoJuego):
    self.niveles = []
    self.hojas = []
    self.nivelActual = 0
    self.nivelPruebaActual = 0
    self.cargarHojas()
    if tipoJuego == 0:
      self.cargarNivelesPrueba()
    else:
      self.cargarNiveles()

  def obtenerNivel(self):
    if self.nivelActual < len(self.niveles):
      nivel = self.niveles[self.nivelActual]
      self.nivelActual += 1
      return nivel
    else:
      return None
      
  def cargarHojas(self):
    x, y = 190, 0
    for hojax in range(self.NUM_HOJAS):
      y = 200
      hojasFila = []
      for hojay in range(self.NUM_HOJAS):
        hojasFila.append(Hoja(x,y, self.RUTA_HOJA))
        y += 100
      self.hojas.append(hojasFila)
      x += 90

  def cargarNivelesPrueba(self):
    index = 0
    
    for iNivelPrueba in range(0, len(self.NUM_SECUENCIAS_NIVEL_PRUEBA)):
      camino = []
      rndInicial = numeroAleatorio(0, self.NUM_HOJAS-1)
      hojaInicial = self.hojas[0][rndInicial]
      rndFinal = numeroAleatorio(0, self.NUM_HOJAS-1)
      hojaFinal = self.hojas[self.NUM_HOJAS -1][rndFinal]
      termino = False
      camino.append(hojaInicial)
      numHojasNivel = self.NUM_SECUENCIAS_NIVEL_PRUEBA[iNivelPrueba]
      while not termino:
        x, y = numeroAleatorio(1, self.NUM_HOJAS-2), numeroAleatorio(0, self.NUM_HOJAS-1)
        miHoja = self.hojas[x][y]
        if len(camino) == numHojasNivel:
          termino = True
        elif miHoja not in camino:
          camino.append(miHoja)
      camino.append(hojaFinal)
      self.niveles.append(Nivel(iNivelPrueba, camino, Nivel.TIPO_NIVEL_PROGRESIVO))
      index = iNivelPrueba

    index += 1
    
    for iNivelPrueba in range(0, len(self.NUM_SECUENCIAS_NIVEL_PRUEBA)):
      nivelPrueba = self.niveles[iNivelPrueba]
      newArray = nivelPrueba.camino[::-1]
      self.niveles.append(Nivel(index, newArray, Nivel.TIPO_NIVEL_REGRESIVO))
      index +=1

  def cargarNiveles(self):
    index = 0

    for iNivel in range(0, len(self.NUM_SECUENCIAS_NIVEL)):
      camino = []
      rndInicial = numeroAleatorio(0, self.NUM_HOJAS-1)
      hojaInicial = self.hojas[0][rndInicial]
      rndFinal = numeroAleatorio(0, self.NUM_HOJAS-1)
      hojaFinal = self.hojas[self.NUM_HOJAS -1][rndFinal]
      termino = False
      camino.append(hojaInicial)
      numHojasNivel = self.NUM_SECUENCIAS_NIVEL[iNivel]
      while not termino:
        x, y = numeroAleatorio(1, self.NUM_HOJAS-2), numeroAleatorio(0, self.NUM_HOJAS-1)
        miHoja = self.hojas[x][y]
        if len(camino) == numHojasNivel:
          termino = True
        elif miHoja not in camino:
          camino.append(miHoja)
      camino.append(hojaFinal)
      self.niveles.append(Nivel(iNivel, camino, Nivel.TIPO_NIVEL_PROGRESIVO))
      index = iNivel
      
    index += 1

    for iNivel in range(0, len(self.NUM_SECUENCIAS_NIVEL)):
      nivel = self.niveles[iNivel]
      newArray = nivel.camino[::-1]
      self.niveles.append(Nivel(index, newArray, Nivel.TIPO_NIVEL_REGRESIVO))
      index +=1
    
class Nivel:
  TIPO_NIVEL_REGRESIVO = "Regresivo"
  TIPO_NIVEL_PROGRESIVO = "Progresivo"
  def __init__(self, numNivel, camino, tipoNivel):
    self.numNivel = numNivel
    self.numPaso = 0
    self.segundos = 0
    self.aciertos = 0
    self.errores = 0
    self.camino = camino
    self.tipoNivel = tipoNivel
    self.indiceMovimiento = 0

  def clickBoton(self, boton):
    if self.camino[self.numPaso] == boton:
      self.aciertos += 1
    else:
      self.errores += 1
    self.numPaso += 1

  def hayMasMovimientos(self):
    return self.numPaso < len(self.camino)

  def obtenerMovimiento(self):
    if self.indiceMovimiento < len(self.camino):
      movimiento = self.camino[self.indiceMovimiento]
      self.indiceMovimiento += 1
      return movimiento
    else:
      return None

class Hoja:
  def __init__(self, x, y, ruta):
    self.x = x
    self.y = y
    self.ruta = ruta