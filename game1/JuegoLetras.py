from game1.utilities import *

class JuegoLetras:
  def __init__(self):
    self.letrasJuego = []
    self.cargarLetrasJuego()
    self.nivelesJuego = []
    self.cargarNivelesJuego()
    self.indiceNivel = 0

  def cargarLetrasJuego(self):
    self.letrasJuego.append(Letra('A',Letra.VOCAL))
    self.letrasJuego.append(Letra('B',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('C',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('D',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('E',Letra.VOCAL))
    self.letrasJuego.append(Letra('F',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('G',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('H',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('I',Letra.VOCAL))
    self.letrasJuego.append(Letra('J',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('K',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('L',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('M',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('N',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('O',Letra.VOCAL))
    self.letrasJuego.append(Letra('P',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('Q',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('R',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('S',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('T',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('U',Letra.VOCAL))
    self.letrasJuego.append(Letra('V',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('W',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('X',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('Y',Letra.CONSONANTE))
    self.letrasJuego.append(Letra('Z',Letra.CONSONANTE))

  def cargarNivelesJuego(self):
    for i in range(1,7):
      arregloLado = [Nivel.IZQ, Nivel.DER]
      lado = arregloLado[numeroAleatorio(0,1)]
      letra = self.letrasJuego[numeroAleatorio(0,len(self.letrasJuego)-1)]
      self.nivelesJuego.append(Nivel(i, lado, letra))
  
  def obtenerNivel(self):
    if self.indiceNivel < len(self.nivelesJuego):
      nivel = self.nivelesJuego[self.indiceNivel]
      self.indiceNivel += 1
      return nivel
    else:
      return None

  def imprimirNiveles(self):
    for nivel in self.nivelesJuego:
      nivel.imprimirNivel()

class Nivel:
  IZQ = 'I'
  DER = 'D'
  TECLA1 = 'Z' 
  TECLA2 = '-'

  def __init__(self, numNivel, lado, letra):
    self.numNivel = numNivel
    self.lado = lado
    self.letra = letra
    self.tiempoReaccion = None
    self.trampa = None
    self.calcularTrampa()
    self.botonPresionado = None

  def calcularTrampa(self):
    if (self.letra.tipoLetra == self.letra.VOCAL and self.lado == self.IZQ) or (self.letra.tipoLetra == self.letra.CONSONANTE and self.lado == self.DER):
      self.trampa = False
    else:
      self.trampa = True

  def presionarBoton(self,tecla):
    self.botonPresionado = tecla

  def imprimirNivel(self):
    print(str(self.numNivel)+" "+str(self.lado)+" "+self.letra.letra+" "+str(self.trampa)+" ")

class Letra:
  VOCAL = 'v'
  CONSONANTE = 'c'
  def __init__(self, letra, tipoLetra):
    self.letra = letra
    self.tipoLetra = tipoLetra
  