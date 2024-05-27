import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from Estructuras.arbol_avl import ArbolAVL
from Objetos.Objeto import Objeto

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ARBOL AVL")
        self.geometry("800x600")

        self.arbol_avl = ArbolAVL()

        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both')

        # Left frame for inputs
        input_frame = ttk.Frame(frame)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # Labels and Entries
        label_valor = ttk.Label(input_frame, text="ID")
        label_valor.grid(row=0, column=0, pady=5, sticky='w')
        self.entry_valor = ttk.Entry(input_frame)
        self.entry_valor.grid(row=0, column=1, pady=5)

        label_nombre = ttk.Label(input_frame, text="Nombre")
        label_nombre.grid(row=1, column=0, pady=5, sticky='w')
        self.entry_nombre = ttk.Entry(input_frame)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        label_color = ttk.Label(input_frame, text="Color")
        label_color.grid(row=2, column=0, pady=5, sticky='w')
        self.entry_color = ttk.Entry(input_frame)
        self.entry_color.grid(row=2, column=1, pady=5)

        self.boton_insertar = ttk.Button(input_frame, text="Insertar", command=self.insertar_valor)
        self.boton_insertar.grid(row=3, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(frame, bg='white', width=600, height=400)
        self.canvas.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)

    def insertar_valor(self):
        valor = int(self.entry_valor.get())
        nombre = self.entry_nombre.get()
        color = self.entry_color.get()
        objeto = Objeto(valor, nombre, color)
        self.arbol_avl.insert(objeto)
        self.dibujar_arbol()

    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self.arbol_avl.raiz is not None:
            self.arbol_avl.dibujar_arbol(self.canvas, self.arbol_avl.raiz, 400, 50, 100, 0)
            
def main():
    root = tk.Tk()  
    root.withdraw()  
    ventana_principal = VentanaPrincipal(root)
    ventana_principal.mainloop()