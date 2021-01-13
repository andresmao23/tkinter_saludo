from tkinter import *
from tkinter import messagebox

class Aplicacion(Frame):
	def __init__(self, ventana=None):
		super().__init__(ventana)
		self.ventana = ventana
		self.grid(column=0, row=0)
		self.crear_widgets()
		
	def crear_widgets(self):
		self.lbl_nombre = Label(self)
		self.lbl_nombre["text"] = "Nombre: "
		self.lbl_nombre.grid(column=0, row=0)
		self.txt_nombre = Entry()
		self.txt_nombre["width"] = 10
		self.txt_nombre.grid(column=1, row=0)
		self.lbl_apellido = Label(self)
		self.lbl_apellido["text"] = "Apellido: "
		self.lbl_apellido.grid(column=0, row=1)
		self.txt_apellido = Entry()
		self.txt_apellido["width"] = 10
		self.txt_apellido.grid(column=1, row=1)
		self.btn_saludar = Button(self)
		self.btn_saludar["text"] = "Saludar"
		self.btn_saludar["command"] = lambda: self.saludar(self.txt_nombre.get(), self.txt_apellido.get())
		self.btn_saludar.grid(column=0, row=2)
		
	def saludar(self, nombre, apellido):
		messagebox.showinfo('Saludar', 'Hola ' + nombre + ' ' + apellido + ', python te saluda!!!')