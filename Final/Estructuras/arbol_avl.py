import tkinter as tk

class Nodo:
    def __init__(self, objeto):
        self.objeto = objeto
        self.izquierda = None
        self.derecha = None
        self.altura = 1

    @property
    def id(self):
        return self.objeto.id

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def rotacion_derecha(self, z):
        y = z.izquierda
        x = y.derecha

        y.derecha = z
        z.izquierda = x

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotacion_izquierda(self, z):
        y = z.derecha
        x = y.izquierda

        y.izquierda = z
        z.derecha = x

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotacion_derecha_izquierda(self, z):
        z.derecha = self.rotacion_derecha(z.derecha)
        return self.rotacion_izquierda(z)

    def rotacion_izquierda_derecha(self, z):
        z.izquierda = self.rotacion_izquierda(z.izquierda)
        return self.rotacion_derecha(z)

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def insert(self, objeto):
        self.raiz = self.insertar(self.raiz, objeto)

    def insertar(self, raiz, objeto):
        if not raiz:
            return Nodo(objeto)
        elif objeto.id < raiz.id:
            raiz.izquierda = self.insertar(raiz.izquierda, objeto)
        else:
            raiz.derecha = self.insertar(raiz.derecha, objeto)

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1:
            if objeto.id < raiz.izquierda.id:
                return self.rotacion_derecha(raiz)
            else:
                raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
                return self.rotacion_derecha(raiz)

        if balance < -1:
            if objeto.id > raiz.derecha.id:
                return self.rotacion_izquierda(raiz)
            else:
                raiz.derecha = self.rotacion_derecha(raiz.derecha)
                return self.rotacion_izquierda(raiz)

        return raiz

    def dibujar_arbol(self, canvas, nodo, x, y, dx, nivel):
        if nodo is not None:
            canvas.create_text(x, y, text=str(nodo.objeto), font=("Helvetica", 12), tags="text")
            if nodo.izquierda:
                canvas.create_line(x, y, x - dx, y + 50, arrow=tk.LAST, tags="line")
                self.dibujar_arbol(canvas, nodo.izquierda, x - dx, y + 50, dx // 2, nivel + 1)
            if nodo.derecha:
                canvas.create_line(x, y, x + dx, y + 50, arrow=tk.LAST, tags="line")
                self.dibujar_arbol(canvas, nodo.derecha, x + dx, y + 50, dx // 2, nivel + 1)




