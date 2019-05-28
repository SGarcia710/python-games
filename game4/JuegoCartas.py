from game4.utilities import *
import os

class JuegoCartas:
  NUM_NIVELES = 6
  MAX_ACIERTOS = 2
  RUTA_CONFIG = 'game4/assets/configs/config.txt'
  RUTA_CARTAS = 'game4/assets/images/'
  def __init__(self):
    self.cartasBase = [] #4
    self.cartasWisconsin = [] #64
    self.niveles = [] # 6
    self.cargarImagenesWisconsin()
    self.cargarCartasBase()
    self.cargarNiveles()
    self.nivelActual = 0

  def calcularResultados(self):
    errores = 0 
    aciertos = 0
    for e in self.niveles:
      errores += e.errores
      aciertos += e.aciertos
    return aciertos, errores

  def obtenerNivel(self):
    if self.nivelActual < len(self.niveles):
        nivel = self.niveles[self.nivelActual]
        self.nivelActual += 1
        return nivel
    else:
        return None

  def cargarImagenesWisconsin(self):
    for root, dirs, files in os.walk(self.RUTA_CARTAS):
      for ruta in files:
        partes = ruta.split('.')
        partes = partes[0].split(',')
        ruta = self.RUTA_CARTAS+ruta
        self.cartasWisconsin.append(Carta(partes[0], partes[1], int(partes[2]), ruta))
  
  def cargarCartasBase(self):
    f = open(self.RUTA_CONFIG, "r")
    lineas = f.readlines()
    for linea in lineas:
      for carta in self.cartasWisconsin:
        if carta.ruta in linea:
          self.cartasBase.append(carta)
          
  def cargarNiveles(self):
    nivelUno = Nivel(self.cartasWisconsin, Nivel.NIVEL_CANTIDAD, 1)
    nivelDos = Nivel(self.cartasWisconsin, Nivel.NIVEL_FORMA, 2)
    nivelTres = Nivel(self.cartasWisconsin, Nivel.NIVEL_COLOR, 3)
    nivelCuatro = Nivel(self.cartasWisconsin, Nivel.NIVEL_CANTIDAD, 4)
    nivelCinco = Nivel(self.cartasWisconsin, Nivel.NIVEL_FORMA, 5)
    nivelSeis = Nivel(self.cartasWisconsin, Nivel.NIVEL_COLOR, 6)
    
    self.niveles.append(nivelUno)
    self.niveles.append(nivelDos)
    self.niveles.append(nivelTres)
    self.niveles.append(nivelCuatro)
    self.niveles.append(nivelCinco)
    self.niveles.append(nivelSeis)
    
class Nivel:
  NIVEL_CANTIDAD = 1
  NIVEL_FORMA = 2
  NIVEL_COLOR = 3
  def __init__(self, cartasWisconsin, tipoNivel, numNivel):
    self.contAciertos = 0
    self.tipoNivel = tipoNivel
    self.numNivel = numNivel
    self.aciertos = 0
    self.errores = 0
    self.carta = None
    self.cartasWisconsin = cartasWisconsin
    
  def cargarCarta(self):
    self.carta = self.cartasWisconsin[numeroAleatorio(0, len(self.cartasWisconsin)-1)]
    return self.carta
    
  def validarJugada(self, ruta):
    for carta in self.cartasWisconsin:
      if carta.ruta == ruta:
        if self.tipoNivel == self.NIVEL_CANTIDAD and carta.cantidad == self.carta.cantidad:
          self.aciertos += 1
          self.contAciertos += 1
        elif self.tipoNivel == self.NIVEL_FORMA and carta.forma == self.carta.forma:
          self.aciertos += 1
          self.contAciertos += 1
        elif self.tipoNivel == self.NIVEL_COLOR and carta.color == self.carta.color:
          self.aciertos += 1
          self.contAciertos += 1
        else:
          self.errores += 1
          self.contAciertos = 0
      
  def ganoNivel(self):
    return True if self.contAciertos == JuegoCartas.MAX_ACIERTOS else False

class Carta: 
  F_TRIANGULO = "triangulo"
  F_ESTRELLA = "estrella"
  F_CRUZ = "cruz"
  F_CIRCULO = "circulo"

  C_AMARILLO = "amarillo"
  C_ROJO = "rojo"
  C_VERDE = "verde"
  C_AZUL = "azul"

  CN_UNO = "uno"
  CN_DOS = "dos"
  CN_TRES = "tres"
  CN_CUATRO = "cuatro"
  def __init__(self, forma, color, cantidad, ruta):
    self.forma = forma
    self.color = color
    self.cantidad = cantidad
    self.ruta = ruta
