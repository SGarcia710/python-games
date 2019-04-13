import random

def numeroAleatorio(x, y):
  return random.randint(x,y)

def desordenarLista(lista):
  random.shuffle(lista)

def guardarLog(cadena):
  file = open("ControlInhibitorio.txt","w") 
  file.write(cadena)
  file.close() 