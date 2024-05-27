class Objeto:
    def __init__(self, id, nombre, color):
        self.id = id
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nColor: {self.color}"
        