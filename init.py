from tkinter import *
from config import *

class Init:
  rootWindow = Tk()
  rootWindow.title("Juegos")
  rootWindow.config(heigh=XY, width=XY)
  rootWindow.configure(bg='white')

  # Gets the requested values of the height and widht.
  windowWidth = rootWindow.winfo_reqwidth()
  windowHeight = rootWindow.winfo_reqheight()
  
  # Gets both half the screen width/height and window width/height
  positionRight = int(rootWindow.winfo_screenwidth()/2 - windowWidth/2)
  positionDown = int(rootWindow.winfo_screenheight()/2 - windowHeight/2)
  
  # Positions the window in the center of the page.
  rootWindow.geometry("+{}+{}".format(positionRight, positionDown))

  title = Label(rootWindow, text = "MENÚ DE JUEGOS", bg = "white")
  title.config(font=("Righteous", 15))
  title.pack()
  title.place(anchor=CENTER, x=XY/2, y= (XY/4))

  btn1 = Button(rootWindow, text="Control Inhibitorio", bg = BLUE, fg = "white", relief = GROOVE, font=("Arial", 11))
  btn1.pack()
  btn1.place(anchor=CENTER, x = (XY/2), y = (XY/2)-35, width = BTNSIZE) 
  btn2 = Button(rootWindow, text="Velocidad de Procesamiento", bg = RED, fg = "white", relief = GROOVE, font=("Arial", 11))
  btn2.pack()
  btn2.place(anchor=CENTER, x = XY/2, y = XY/2, width = BTNSIZE)
  btn3 = Button(rootWindow, text="Memoria de Trabajo Fonológica", bg = GREEN, fg = "white", relief = GROOVE, font=("Arial", 11))
  btn3.pack()
  btn3.place(anchor=CENTER, x = (XY/2), y = (XY/2)+35, width = BTNSIZE )
  btn4 = Button(rootWindow, text="Logs", bg = DARK, fg = "white", relief = GROOVE)
  btn4.pack()
  btn4.place(anchor=CENTER, x = XY-30, y = XY-17, width = 50 )

  rootWindow.mainloop()