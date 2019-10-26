from game4.utilities import *
import os
from game4.Queue import Queue as q

class JuegoNumeros:
  MAX_ACIERTOS = 10
  MAX_NIVELES = 3
  def __init__(self):
    self.niveles = []
    self.cargarNiveles()
    self.nivelActual = 0

  def obtenerNivel(self):
    if self.nivelActual < len(self.niveles):
      nivel = self.niveles[self.nivelActual]
      self.nivelActual += 1
      return nivel
    else:
      return None

  def cargarNiveles(self):
    cola = q()
    cola.enqueue(1)
    cola.enqueue(2)
    cola.enqueue(3)
    for i in range(self.MAX_NIVELES):
      descolado = cola.dequeue()
      self.niveles.append(Nivel(descolado))
      cola.enqueue(descolado)
  
  def calcularResultados(self):
    errores = 0 
    aciertos = 0
    for e in self.niveles:
      errores += e.errores
      aciertos += e.aciertos
    return aciertos, errores

class Nivel:
  MAX_PISTAS_POR_NIVEL = 3
  def __init__(self, tipoOperacion):
    self.contAciertos = 0
    self.tipoOperacion = tipoOperacion
    self.aciertos = 0
    self.errores = 0
    self.pistasMostradas = 0
    self.operacion = None
    self.cargarOperacion()
  
  def cargarOperacion(self):
    hayPista = True if numeroAleatorio(0,1) == 1 else False
    if hayPista and self.pistasMostradas < self.MAX_PISTAS_POR_NIVEL:
      self.operacion = Operacion(self.tipoOperacion, hayPista)
      self.pistasMostradas += 1
    else:
      self.operacion = Operacion(self.tipoOperacion, False)
    

  def presionarBoton(self, numero):
    for i in range(0, len(self.operacion.numerosUsuario)):
      if self.operacion.numerosUsuario[i] is -1:
        self.operacion.numerosUsuario[i] = numero
        break

  def botonesPresionados(self):
    return True if -1 not in self.operacion.numerosUsuario else False

  def validarRonda(self):
    if self.operacion.numerosUsuario[2] == self.operacion.numeros[2]:
      self.contAciertos += 1
      self.aciertos += 1
    else:
      self.errores += 1
      self.contAciertos = 0
    self.cargarOperacion()

  def ganoNivel(self):
    return True if self.contAciertos == JuegoNumeros.MAX_ACIERTOS else False

class Operacion:
  SUMA = 1
  RESTA = 2
  MULTIPLICACION = 3
  def __init__(self, tipoOperacion, hayPista):
    self.tipoOperacion = tipoOperacion
    self.numeros = [] #3 numeros de la operacion
    self.listaNumeros = [] #los 4 numeros de los botones, desordenados
    self.numerosUsuario = [-1, -1, -1]
    self.hayPista = hayPista
    self.crearOperacion()
  def crearOperacion(self):
    rango = None
    if self.tipoOperacion is self.SUMA or self.tipoOperacion is self.RESTA:
      rango = [1, 50]
    else:
      rango = [1, 9]
    
    #Numeros de la Logica
    self.numeros.append(numeroAleatorio(rango[0], rango[1]))
    self.numeros.append(numeroAleatorio(rango[0], rango[1]))
    
    #Genero resultado de la Logica
    if self.tipoOperacion is self.SUMA:
      self.numeros.append(self.numeros[0] + self.numeros[1])
    elif self.tipoOperacion is self.RESTA:
      if self.numeros[0] > self.numeros[1]:
        self.numeros.append(self.numeros[0] - self.numeros[1])
      else:
        tempB = self.numeros[1]
        self.numeros[1] = self.numeros[0]
        self.numeros[0] = tempB
        self.numeros.append(self.numeros[0] - self.numeros[1])        
    else: 
      self.numeros.append(self.numeros[0] * self.numeros[1])
    
    #hago lista de numeros para vista
    self.listaNumeros.append(self.numeros[0])
    self.listaNumeros.append(self.numeros[1])
    self.listaNumeros.append(self.numeros[2])
    
    #pista
    if self.hayPista:
        indexAleatorio = numeroAleatorio(0,2)
        self.numerosUsuario[indexAleatorio] = self.numeros[indexAleatorio]


    tempComodin = numeroAleatorio(rango[0], rango[1])
    while tempComodin in self.listaNumeros:
      tempComodin = numeroAleatorio(rango[0], rango[1])
    self.listaNumeros.append(tempComodin)
    desordenarLista(self.listaNumeros)