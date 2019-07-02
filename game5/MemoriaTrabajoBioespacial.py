from tkinter import *
from game5.utilities import *
from game5.InstruccionesNivelUno import *

class MemoriaTrabajoBioespacial:
  def __init__(self, menuWindow):  
    self.menuWindow = menuWindow
    self.rootWindow = Tk()
    self.rootWindow.title("Memoria Trabajo Bioespacial")
    self.rootWindow.config(heigh=XY, width=XY)
    self.rootWindow.configure(bg='white')

    self.windowWidth = self.rootWindow.winfo_reqwidth()
    self.windowHeight = self.rootWindow.winfo_reqheight()

    self.positionRight = int(self.rootWindow.winfo_screenwidth()/2 - self.windowWidth/2)
    self.positionDown = int(self.rootWindow.winfo_screenheight()/2 - self.windowHeight/2)

    self.rootWindow.geometry("+{}+{}".format(self.positionRight, self.positionDown))

    self.title = Label(self.rootWindow, text = "MENÚ MEM. TRAB. BIOESPACIAL", bg = "white")
    self.title.config(font=("Righteous", 14))
    self.title.place(anchor=CENTER, x=XY/2, y= (XY/4))

    self.btn1 = Button(self.rootWindow, text="INICIAR JUEGO", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11), command = self.iniciarInstruccionesUno)
    self.btn1.place(anchor=CENTER, x = (XY/2), y = XY/2, width = BTNSIZE) 
    self.btn4 = Button(self.rootWindow, text="Logs", bg = DARK, fg = "white", relief = GROOVE, command = abrirArchivo)
    self.btn4.place(anchor=CENTER, x = XY-30, y = XY-17, width = 50 )
    self.btn5 = Button(self.rootWindow, text="Menú", bg = DARK, fg = "white", relief = GROOVE, command = self.volverMenu)
    self.btn5.place(anchor=CENTER, x = 30, y = XY-17, width = 50 )

    self.rootWindow.mainloop()
    
  def iniciarInstruccionesUno(self):
    self.rootWindow.withdraw()
    numeros = InstruccionesNivelUno(self.rootWindow)

  def volverMenu(self):
    self.rootWindow.destroy()
    self.menuWindow.deiconify()