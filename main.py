from Estructuras.binary_search_tree import BinarySearchTree

#hola
class PolynomialMenu:
    def __init__(self):
        self.poly1 = []
        self.poly2 = []
        self.arbol1 = BinarySearchTree()
        self.arbol2 = BinarySearchTree()

    def ingresar_polinomio(self):
        # Ingresar el primer polinomio
        grado1 = int(input("Ingresa el grado del primer polinomio: "))
        for i in range(grado1 + 1):
            coef = float(input(f"Ingresa el coeficiente para x^{i}: "))
            self.arbol1.insert(i, coef)
        
        # Ingresar el segundo polinomio
        grado2 = int(input("Ingresa el grado del segundo polinomio: "))
        for i in range(grado2 + 1):
            coef = float(input(f"Ingresa el coeficiente para x^{i}: "))
            self.arbol2.insert(i, coef)

        print("Primer polinomio ingresado:")
        self.arbol1.print_in_order()
        print("Segundo polinomio ingresado:")
        self.arbol2.print_in_order()

    def opcion_2(self):
        # Aquí podrías implementar adición y sustracción
        print("Adición y Sustracción de polinomios (No implementado)")

    def opcion_3(self):
        # Aquí podrías implementar la evaluación de polinomios
        print("Evaluación de polinomios (No implementado)")

    def mostrar_menu(self):
        print("\nMENU DE POLINOMIOS")
        print("1. Ingresar Componentes Polinomios")
        print("2. Adiccion y Sustraccion")
        print("3. Evaluar Polinomios")
        print("4. Salir")

        opcion = 0
        while opcion != 4:
            try:
                opcion = int(input("Selecciona una opción (1-4): "))
                if opcion == 1:
                    self.ingresar_polinomio()
                elif opcion == 2:
                    self.opcion_2()
                elif opcion == 3:
                    self.opcion_3()
                elif opcion == 4:
                    print('Saliendo del Programa...')
                    break
                else:
                    print("Opción no válida, por favor intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

if __name__ == '__main__':
    menu = PolynomialMenu()
    menu.mostrar_menu()

