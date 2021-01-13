import tkinter as tk
from vista.aplicacion import Aplicacion

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(ventana=root)
    app.mainloop()