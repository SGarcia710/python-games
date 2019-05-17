from game3.utilities import *
import os


class JuegoSonidos:

    RUTA_SONIDOS = "game3/assets/sonidos"
    RUTA_CONFIG = "game3/assets/configs/config.txt"
    def __init__(self):
        self.nivelActual = 0
        self.sonidos = []
        self.niveles = []
        self.cargarSonidos()
        self.cargarNiveles()

    def calcularResultados(self):
        aciertos = 0
        errores = 0
        for nivel in self.niveles:
            if nivel.nivelCorrecto:
                aciertos += 1
            else:
                errores += 1
        return aciertos, errores

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
                ruta = self.RUTA_SONIDOS + "/" + ruta
                self.sonidos.append(Sonido(ruta, palabra, esMonosilaba))

    def cargarNiveles(self):
        f = open(self.RUTA_CONFIG, "r")
        niveles = int(f.readline().split("=")[1])
        i = 0
        while i < niveles:
            i += 1
            linea = f.readline()
            linea = linea.split(";")
            numNivel = int(linea[0].split("=")[1])
            sonidosTexto = linea[1].split("=")[1].split(",")
            sonidosFiltrados = []
            for sn in sonidosTexto:
                for sonido in self.sonidos:
                    if sonido.palabra in sn:
                        sonidosFiltrados.append(sonido)
            self.niveles.append(Nivel(numNivel, sonidosFiltrados))

class Nivel:

    def __init__(self, numNivel, sonidos):
        self.numNivel = numNivel
        self.sonidos = sonidos
        self.nivelCorrecto = None
        self.sonidoActual = 0

    def imprimirSonidos(self):
        for sonido in self.sonidos:
            print(sonido.palabra)

    def calificarNivel(self, nivelCorrecto):
        self.nivelCorrecto = nivelCorrecto

    def sonidoFinal(self):
        return True if self.sonidoActual == (len(self.sonidos) -1) else False

    def obtenerSonidoNivel(self):
        if self.sonidoActual < len(self.sonidos):
            sonido = self.sonidos[self.sonidoActual]
            self.sonidoActual += 1
            return sonido
        else:
            return None

    def elSonidoEsCorrecto(self, palabra):
        sNivel = None
        for sonido in self.sonidos:
            if sonido.palabra == palabra:
                sNivel = sonido
        sonidoNivel = self.obtenerSonidoNivel()
        return True if sNivel == sonidoNivel else False

class Sonido:

    def __init__(self, ruta, palabra, esMonosilaba):
        self.ruta = ruta
        self.palabra = palabra
        self.esMonosilaba = esMonosilaba
