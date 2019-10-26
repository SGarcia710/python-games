import os
from game2.utilities import *

class VelocidadProcesamiento:
  JUEGO_UNO = 1
  JUEGO_DOS = 2
  CANT_SECU_UNO = 5
  CANT_SECU_DOS = 6
  RUTA_ICONOS = "game2/assets/icons"
  RUTA_IMAGENES = "game2/assets/images"
  def __init__(self, tipo):
    self.tipoJuego = tipo
    self.nivelActual = 0
    self.ilustraciones = []
    self.iconos = []
    self.niveles = []
    self.crearIlustraciones()
    self.crearIconos()
    self.crearNiveles()

  def obtenerNivel(self):
    if self.nivelActual < len(self.niveles):
      nivel = self.niveles[self.nivelActual]
      self.nivelActual += 1
      return nivel
    else:
      return None

  def calcularResultados(self):
    aciertos = 0
    fallos = 0
    for nivel in self.niveles:
      resLocal = False
      for ilustracion in nivel.ilustraciones:
        if self.tipoJuego == self.JUEGO_UNO:
          comparador = nivel.icono.palabra
          paquete = ilustracion.palabras
        else:
          comparador = nivel.icono.palabra[0]
          paquete = ilustracion.iniciales
        if comparador in str(paquete):
          resLocal = True
          break
      if resLocal and nivel.resultado == nivel.RES_SI:
        aciertos += 1
      elif not resLocal and nivel.resultado == nivel.RES_NO:
        aciertos += 1
      else:
        fallos += 1
    return aciertos, fallos
  
  def crearIlustraciones(self):
    for root, dirs, files in os.walk(self.RUTA_IMAGENES):
      for fileName in files:
        palabras = fileName.split(".")[0].split(",")
        iniciales = []
        for palabra in palabras: 
          iniciales.append(palabra[0])
        ruta = self.RUTA_IMAGENES + "/" + fileName
        self.ilustraciones.append(Ilustracion(ruta, palabras, iniciales))

  def crearIconos(self):
    for root, dirs, files in os.walk(self.RUTA_ICONOS):
      for fileName in files:
        palabra = fileName.split(".")[0]
        ruta = self.RUTA_ICONOS + "/" + fileName
        self.iconos.append(Icono(ruta, palabra))

  def crearNiveles(self):
    if self.tipoJuego == self.JUEGO_UNO:      
      for i in range(self.CANT_SECU_UNO):
        numeros = numSinRepetir(3, len(self.ilustraciones)-1)
        ilustracionesRand = []
        ilustracionesRand.append(self.ilustraciones[numeros[0]])
        ilustracionesRand.append(self.ilustraciones[numeros[1]])
        ilustracionesRand.append(self.ilustraciones[numeros[2]])
        iconoRand = self.iconos[numeroAleatorio(0,len(self.iconos)-1)]
        self.niveles.append(Nivel(i, ilustracionesRand, iconoRand))
    else:
      for i in range(self.CANT_SECU_DOS):
        numeros = numSinRepetir(3, len(self.ilustraciones)-1)
        ilustracionesRand = []
        ilustracionesRand.append(self.ilustraciones[numeros[0]])
        ilustracionesRand.append(self.ilustraciones[numeros[1]])
        ilustracionesRand.append(self.ilustraciones[numeros[2]])
        iconoRand = self.iconos[numeroAleatorio(0,len(self.iconos)-1)]
        self.niveles.append(Nivel(i, ilustracionesRand, iconoRand))

class Nivel:
  RES_SI = "SI"
  RES_NO = "NO"
  def __init__(self, numNivel, ilustraciones, icono):
    self.numNivel = numNivel
    self.resultado = None
    self.tiempo = 0
    self.ilustraciones = ilustraciones #arreglo de 3
    self.icono = icono

  def actualizarTiempo(self, tiempo):
    self.tiempo = tiempo
  def registrarResultado(self, resultado):
    self.resultado = resultado

class Icono:
  def __init__(self, ruta, palabra):
    self.ruta = ruta
    self.palabra = palabra

class Ilustracion: 
  def __init__(self, ruta, palabras, iniciales):
    self.ruta = ruta
    self.palabras = palabras
    self.iniciales = iniciales