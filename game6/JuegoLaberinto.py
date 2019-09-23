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
    for index, row in enumerate(spamreader):
      textoNivel = row[0]
      metas = row[1]
      metas = metas.split('-')
      metasNivel = []
      for meta in metas:
        meta = meta.split('_')
        coord1 = meta[0]
        coord1 = coord1.replace('[', '')
        coord1 = coord1.split(',')
        xMin = coord1[0]
        xMin = xMin.replace('(', '')
        xMin = int(xMin)
        yMin = coord1[1]
        yMin = yMin.replace(')', '')
        yMin = int(yMin)
        coord2 = meta[1]
        coord2 = coord2.replace(']', '')
        coord2 = coord2.split(',')
        xMax = coord2[0]
        xMax = xMax.replace('(', '')
        xMax = int(xMax)
        yMax = coord2[1]
        yMax = yMax.replace(')', '')
        yMax = int(yMax)
        metasNivel.append(Coordenada(xMin, yMin, xMax, yMax))

      trampas = row[2]
      trampas = trampas.split('-')
      trampasNivel = []
      for trampa in trampas:
        if trampa != '':
          trampa = trampa.split('_')
          coord1 = trampa[0]
          coord1 = coord1.replace('[', '')
          coord1 = coord1.split(',')
          xMin = coord1[0]
          xMin = xMin.replace('(', '')
          xMin = int(xMin)
          yMin = coord1[1]
          yMin = yMin.replace(')', '')
          yMin = int(yMin)
          coord2 = trampa[1]
          coord2 = coord2.replace(']', '')
          coord2 = coord2.split(',')
          xMax = coord2[0]
          xMax = xMax.replace('(', '')
          xMax = int(xMax)
          yMax = coord2[1]
          yMax = yMax.replace(')', '')
          yMax = int(yMax)
          trampasNivel.append(Coordenada(xMin, yMin, xMax, yMax))
      ruta = row[3]
      coordenadaInicial = row[4]
      coordenadaInicial = coordenadaInicial.split(',')
      xInicial = int(coordenadaInicial[0])
      yInicial = int(coordenadaInicial[1])
      nivel = Nivel(index, ruta, metasNivel, trampasNivel, xInicial, yInicial)
      self.niveles.append(nivel

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