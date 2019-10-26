from tkinter import *
from config import *
from game1.ControlInhibitorio import ControlInhibitorio
from game2.VelocidadProcesamiento import VelocidadProcesamiento
from game3.MemoriaTrabajoFonologica import MemoriaTrabajoFonologica
from game4.FlexibilidadCognitiva import FlexibilidadCognitiva
from game5.MemoriaTrabajoBioespacial import MemoriaTrabajoBioespacial
from game6.PlaneacionYOrganizacion import PlaneacionYOrganizacion

class Juegos:
  def __init__(self):
    self.rootWindow = Tk()
    
    self.rootWindow.title("Juegos")
    self.rootWindow.config(heigh=XY, width=XY)
    self.rootWindow.configure(bg='white')

    windowWidth = self.rootWindow.winfo_reqwidth()
    windowHeight = self.rootWindow.winfo_reqheight()
    
    positionRight = int(self.rootWindow.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(self.rootWindow.winfo_screenheight()/2 - windowHeight/2)
    
    self.rootWindow.geometry("+{}+{}".format(positionRight, positionDown))

    title = Label(self.rootWindow, text = "MENÚ DE JUEGOS", bg = "white")
    title.config(font=("Righteous", 15))
    title.pack()
    title.place(anchor=CENTER, x=XY/2, y= (XY/4)-35)

    #Sapo
    btn5 = Button(self.rootWindow, text="Memoria de Trabajo Bioespacial", bg = BANANA, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarMemTrabBio)
    btn5.pack()
    btn5.place(anchor=CENTER, x = (XY/2), y = (XY/2)-35-35, width = BTNSIZE )
    #Audios
    btn3 = Button(self.rootWindow, text="Memoria de Trabajo Fonológica", bg = AURORAGREEN, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarMemFono)
    btn3.pack()
    btn3.place(anchor=CENTER, x = (XY/2), y = (XY/2)-35, width = BTNSIZE )
    #Globos y Letras
    btn2 = Button(self.rootWindow, text="Velocidad de Procesamiento", bg = MANDARINRED, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarVelocidadP)
    btn2.pack()
    btn2.place(anchor=CENTER, x = XY/2, y = XY/2, width = BTNSIZE)
    #Imagenes y Palabras
    btn1 = Button(self.rootWindow, text="Control Inhibitorio", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarControlI)
    btn1.pack()
    btn1.place(anchor=CENTER, x = (XY/2), y = (XY/2)+35, width = BTNSIZE) 
    #Nivel 1: Laberinto con Mouse
    btn6 = Button(self.rootWindow, text="Planeacion y Organizacion", bg = PURPLE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarPlanYOrg)
    btn6.pack()
    btn6.place(anchor=CENTER, x = (XY/2), y = (XY/2)+35+35, width = BTNSIZE )
    #Cartas y Operaciones
    btn4 = Button(self.rootWindow, text="Flexibilidad Cognitiva", bg = JALAPENORED, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarFlexCogni)
    btn4.pack()
    btn4.place(anchor=CENTER, x = (XY/2), y = (XY/2)+35+35+35, width = BTNSIZE)

    self.rootWindow.mainloop()

  def iniciarControlI(self):
    self.rootWindow.withdraw()
    ctrlI = ControlInhibitorio(self.rootWindow)
  
  def iniciarVelocidadP(self):
    self.rootWindow.withdraw()
    velP = VelocidadProcesamiento(self.rootWindow)

  def iniciarMemFono(self):
    self.rootWindow.withdraw()
    mf = MemoriaTrabajoFonologica(self.rootWindow)

  def iniciarFlexCogni(self):
    self.rootWindow.withdraw()
    fc = FlexibilidadCognitiva(self.rootWindow)

  def iniciarMemTrabBio(self):
    self.rootWindow.withdraw()
    fc = MemoriaTrabajoBioespacial(self.rootWindow)

  def iniciarPlanYOrg(self):
    self.rootWindow.withdraw()
    pyo = PlaneacionYOrganizacion(self.rootWindow)