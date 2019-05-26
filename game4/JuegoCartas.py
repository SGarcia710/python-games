from game4.utilities import *
import os

class JuegoCartas:
  NUM_NIVELES = 6
  MAX_ACIERTOS = 10
  RUTA_CONFIG = 
  RUTA_CARTAS = 
  def __init__(self):
    self.cartasBase = [] #4
    self.cartasWisconsin = [] #64
    self.niveles = [] # 6

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

class Carta: 
  F_TRIANGULO = 1
  F_ESTRELLA = 2
  F_CRUZ = 3
  F_CIRCULO = 4

  C_AMARILLO = 1
  C_ROJO = 2
  C_VERDE = 3
  C_AZUL = 4

  CN_UNO = 1
  CN_DOS = 2
  CN_TRES = 3
  CN_CUATRO = 4
    def __init__(self, forma, color, cantidad):
      self.forma = forma
      self.color = color
      self.cantidad = cantidad
      self.ruta