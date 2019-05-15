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
                nivelPalabra = int(caracteristicas[2])
                self.sonidos.append(Sonido(ruta, palabra, esMonosilaba, nivelPalabra))

    def cargarNiveles(self):
        f = open(self.RUTA_CONFIG, "r")
        print(f.readline())

class Nivel:

    def __init__(self, numNivel, sonidos):
        self.sonidos = sonidos
        self.numNivel = numNivel
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
        sNivel = sonidos[sNivel for sNivel in sonidos if sNivel.sonido.palabra = palabra]
        sonidoNivel = self.__obtenerSonidoNivel()
        return True if sNivel == sonidoNivel else False

class Sonido:

    def __init__(self, ruta, palabra, esMonosilaba, nivelPalabra):
        self.ruta = ruta
        self.palabra = palabra
        self.esMonosilaba = esMonosilaba
        self.nivelPalabra = nivelPalabra
