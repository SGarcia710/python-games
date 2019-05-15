from game3.utilities import *
import os


class JuegoSonidos:

    RUTA_SONIDOS = "game3/assets/sonidos"
    RUTA_CONFIG = "game3/assets/config/config.txt"
    def __init__(self):
        self.nivelActual = 0
        self.sonidos = []
        self.niveles = []
        self.cargarSonidos()
        self.cargarNiveles()

    def obtenerNivel(self):
        if self.nivelActual < len(self.niveles):
            nivel = self.niveles[self.nivelActual]
            self.nivelActual += 1
            return nivel
        else:
            return None

    def cargarSonidos(self):
        for root, dirs, files in os.walk(self.RUTA_SONIDOS):
            for ruta in files:
                caracteristicas = ruta.split(".")[0].split(",")
                palabra = caracteristicas[0]
                esMonosilaba = True if caracteristicas[1] == 'si' else False
                self.sonidos.append(Sonido(ruta, palabra, esMonosilaba))

    def cargarNiveles(self):
        f = open(self.RUTA_CONFIG, "r")
        linea = f.readline()
        while linea is not None:
            linea = linea.split(";")
            numNivel = int(linea[0].split("=")[1])
            sonidosTexto = linea[1].split("=")[1].split(",")
            sonidosFiltrados = [sonido for sonido in sonidos if sonido.palabra in sonidosTexto]
            self.niveles.append(Nivel(numNivel, sonidosFiltrados))
            linea = f.readline()

class Nivel:

    def __init__(self, numNivel, sonidos):
        self.numNivel = numNivel
        self.sonidos = sonidos
        self.nivelCorrecto = None
        self.sonidoActual = 0

    def calificarNivel(self, nivelCorrecto):
        self.nivelCorrecto = nivelCorrecto

    def sonidoFinal(self):
        return True if self.sonidoActual == ((self.sonidos) -1) else False

    def __obtenerSonidoNivel(self):
        if self.sonidoActual < len(self.sonidos):
            sonido = self.sonido[self.sonidoActual]
            self.sonidoActual += 1
            return sonido
        else:
            return None

    def elSonidoEsCorrecto(self, palabra):
        sNivel = sonidos[sNivel for sNivel in sonidos if sNivel.palabra = palabra]
        sonidoNivel = self.__obtenerSonidoNivel()
        return True if sNivel == sonidoNivel else False

class Sonido:

    def __init__(self, ruta, palabra, esMonosilaba):
        self.ruta = ruta
        self.palabra = palabra
        self.esMonosilaba = esMonosilaba