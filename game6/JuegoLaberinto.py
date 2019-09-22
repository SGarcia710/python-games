from game6.utilities import *

class JuegoLaberinto:
  def __init__(self, tipoJuego):

  # def generarResultados(self):
  #   resultadosRondas = ""
  #   for nivel in self.niveles:
  #     segundos = nivel.segundos % 60
  #     minutos = int(nivel.segundos / 60)
  #     resultadosRondas += "\tRonda "+str(nivel.numNivel)+": Aciertos: "+str(nivel.aciertos)+", Errores: "+str(nivel.errores)+", Tiempo: "+str(minutos)+":"+str(segundos)+"m.\n"
  #   return resultadosRondas

  # def obtenerNivel(self):
  #   if self.nivelActual < len(self.niveles):
  #     nivel = self.niveles[self.nivelActual]
  #     self.nivelActual += 1
  #     return nivel
  #   else:
  #     return None
      
class Nivel:
  def __init__(self):

