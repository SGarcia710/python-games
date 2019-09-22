import csv

class JuegoLaberinto:

  RUTA_PUNTERO = '.../...'
  RUTA_NIVELES = 'game6/assets/config/config.csv'
  def __init__(self):
    self.niveles = []
    self.nivelActual=None
    self.cargarNiveles()

  def cargarNiveles(self):
    csvfile = open(self.RUTA_NIVELES)
    spamreader  = csv.reader(csvfile, delimiter=';')

    
  

class Nivel:
  def __init__(self, numNivel, rutaImagen, metas, trampas, xInicial, yInicial):
    self.numNivel = numNivel
    self.rutaImagen = rutaImagen
    self.metas = metas
    self.trampas = trampas

class Coordenada:
  def __init__(self, minX, minY, maxX, maxY):
    self.minX = minX
    self.minY = minY
    self.maxX = maxX
    self.maxY = maxY