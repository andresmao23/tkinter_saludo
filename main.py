import tkinter as tk
from vista.aplicacion import Aplicacion

if __name__ == "__main__":
    root = tk.Tk()
    # Crea la aplicación
    app = Aplicacion(ventana=root)
    #
    # here are method calls to the window manager class
    #
    app.ventana.title("Proyecto para saludar a una persona")
    app.ventana.maxsize(1000, 400)
    # start the program
    app.mainloop()