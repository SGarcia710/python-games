import random
import os

XY = 300
BTNSIZE = 210
BLUE = "#01CBCF"
RED = "#f96262"
GREEN = "#0ce59a"
DARK = "#404e67"
archivoTXT = "game1/ControlInhibitorio.txt"

def numeroAleatorio(x, y):
  return random.randint(x,y)

def desordenarLista(lista):
  random.shuffle(lista)

def guardarLog(cadena):
  file = open(archivoTXT,"a") 
  file.write(cadena)
  file.close() 

def abrirArchivo():
  string = "notepad.exe "+ archivoTXT
  os.system(string)