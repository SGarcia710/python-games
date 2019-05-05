from game1.utilities import *

class JuegoLetras:
  NUMERO_NIVELES_TOTAL = 30 
  NUMERO_NIVELES_OK = int(NUMERO_NIVELES_TOTAL * 0.80)
  NUMERO_NIVELES_TRAMPA = int(NUMERO_NIVELES_TOTAL * 0.20)
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
    for i in range(self.NUMERO_NIVELES_OK):
      letra = self.letrasJuego[numeroAleatorio(0,len(self.letrasJuego)-1)]
      if letra.tipoLetra == letra.VOCAL:
        self.nivelesJuego.append(Nivel(Nivel.IZQ, letra))
      else:
        self.nivelesJuego.append(Nivel(Nivel.DER, letra))
    for i in range(self.NUMERO_NIVELES_TRAMPA):
      letra = self.letrasJuego[numeroAleatorio(0,len(self.letrasJuego)-1)]
      if letra.tipoLetra == letra.VOCAL:
        self.nivelesJuego.append(Nivel(Nivel.DER, letra))
      else:
        self.nivelesJuego.append(Nivel(Nivel.IZQ, letra))
    desordenarLista(self.nivelesJuego)
  
  def obtenerNivel(self):
    if self.indiceNivel < len(self.nivelesJuego):
      nivel = self.nivelesJuego[self.indiceNivel]
      self.indiceNivel += 1
      return nivel
    else:
      return None

  def calcularResultados(self):
    aciertos = 0
    errores = 0
    for nivel in self.nivelesJuego:
      if nivel.trampa == True:
        if nivel.botonPresionado == None:
          aciertos += 1
        else:
          errores += 1
      else:
        if nivel.lado == nivel.IZQ and nivel.letra.tipoLetra == nivel.letra.VOCAL:
          if nivel.botonPresionado == nivel.TECLA1:
            aciertos += 1
          else:
            errores += 1 
        else:
          if nivel.lado == nivel.DER and nivel.letra.tipoLetra == nivel.letra.CONSONANTE:
            if nivel.botonPresionado == nivel.TECLA2:
              aciertos += 1              
            else:
              errores += 1 
    return aciertos, errores

class Nivel:
  #Izquierda Vocal
  #derecha Consonante
  IZQ = 'I'
  DER = 'D'
  TECLA1 = 'Z' 
  TECLA2 = '-'

  def __init__(self, lado, letra):
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

  def presionarBoton(self, tecla):
    self.botonPresionado = tecla

class Letra:
  VOCAL = 'v'
  CONSONANTE = 'c'
  def __init__(self, letra, tipoLetra):
    self.letra = letra
    self.tipoLetra = tipoLetra