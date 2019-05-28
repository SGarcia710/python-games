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
    def __init__(self, forma, color, cantidad):
      self.forma = forma
      self.color = color
      self.cantidad = cantidad
      self.ruta