from Estructuras.binary_search_tree import BinarySearchTree


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

    def sumar_polinomios(self):
        suma_arbol = self.arbol1.sumar_arboles(self.arbol2)
        print("Resultado de la suma:")
        suma_arbol.print_in_order()

    def restar_polinomios(self):
        resta_arbol = self.arbol1.restar_arboles(self.arbol2)
        print("Resultado de la resta:")
        resta_arbol.print_in_order()

    def mostrar_menu(self):
        print("\nMENU DE POLINOMIOS")
        print("1. Ingresar Componentes Polinomios")
        print("2. Adiccion y Sustraccion")
        print("3. Evaluar Polinomios")
        print("4. Reiniciar Polinomios (Limpiar Estructuras)")
        print("5. Salir")

        opcion = 0
        while opcion != 5:
            try:
                opcion = int(input("Selecciona una opción (1-5): "))
                if opcion == 1:
                    self.ingresar_polinomio()
                elif opcion == 2:
                    print("\nMENU DE OPERACIONES POLINOMIOS")
                    print("1. Sumar")
                    print("2. Restar")
                    print("3. Salir")

                    seleccion = 0
                    while seleccion != 4:
                        try:
                            seleccion = int(input("Selecciona una opción (1-3): "))
                            if seleccion == 1:
                                self.sumar_polinomios()
                            elif seleccion == 2:
                                self.restar_polinomios()
                            elif seleccion == 3:
                                print('Saliendo...')
                                break
                            else:
                                print("Opción no válida, por favor intenta de nuevo.")
                        except ValueError:
                            print("Por favor, ingresa un número válido.")
                elif opcion == 3:
                    # Ingresar los polinomios
                    x_value = float(input("Ingresa el valor de x para evaluar los polinomios: "))
                    result_poly1 = self.arbol1.evaluate(x_value)
                    result_poly2 = self.arbol2.evaluate(x_value)      
                    print("Resultado de evaluar el primer polinomio:", result_poly1)
                    print("Resultado de evaluar el segundo polinomio:", result_poly2)
                elif opcion == 4:
                    self.arbol1.clear()
                    self.arbol2.clear()    
                    print("Memoria vaciada, puede ingresar nuevos polinomios.")
                elif opcion == 5:
                    print('Saliendo del Programa...')
                    break
                else:
                    print("Opción no válida, por favor intenta de nuevo.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

if __name__ == '__main__':
    menu = PolynomialMenu()
    menu.mostrar_menu()

