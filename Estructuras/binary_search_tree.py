from Estructuras.node import Node
from typing import  Generic, Optional, TypeVar
T = TypeVar("T")

class BinarySearchTree:
    def __init__(self):
        self.__root = None 

    def insert(self, degree, coef):
        if not self.__root:
            self.__root = Node(degree, coef)
        else:
            self._insert_recursive(self.__root, degree, coef)

    def _insert_recursive(self, node, degree, coef):
        if degree < node.degree:
            if not node.left:
                node.left = Node(degree, coef)
            else:
                self._insert_recursive(node.left, degree, coef)
        elif degree > node.degree:
            if not node.right:
                node.right = Node(degree, coef)
            else:
                self._insert_recursive(node.right, degree, coef)
        else:
            node.coef += coef 

    def print_in_order(self):
        self._print_in_order(self.__root)
        print()

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(f"{node.coef}x^{node.degree}", end=' + ')
            self._print_in_order(node.right)

    def sumar_arboles(self, other_tree):
        result_tree = BinarySearchTree()
        self._sumar_arboles_recursive(self.__root, other_tree.__root, result_tree)
        return result_tree

    def _sumar_arboles_recursive(self, node1, node2, result_tree):
        stack1 = []
        stack2 = []
        current1 = node1
        current2 = node2

        while current1 or stack1 or current2 or stack2:
            while current1:
                stack1.append(current1)
                current1 = current1.left
            while current2:
                stack2.append(current2)
                current2 = current2.left

            if stack1:
                current1 = stack1.pop()
            if stack2:
                current2 = stack2.pop()

            if current1 and current2:
                if current1.degree == current2.degree:
                    print("Sumando coeficientes de x^" + str(current1.degree))
                    result_node = result_tree.search(current1.degree)
                    if result_node:
                        result_node.coef += current1.coef
                        result_node.coef += current2.coef
                    else:
                        result_tree.insert(current1.degree, current1.coef + current2.coef)
                    current1 = current1.right
                    current2 = current2.right
                elif current1.degree < current2.degree:
                    result_tree.insert(current1.degree, current1.coef)
                    current1 = current1.right
                else:
                    result_tree.insert(current2.degree, current2.coef)
                    current2 = current2.right
            elif current1:
                result_tree.insert(current1.degree, current1.coef)
                current1 = current1.right
            elif current2:
                result_tree.insert(current2.degree, current2.coef)
                current2 = current2.right

        return result_tree

    def restar_arboles(self, other_tree):
        result_tree = BinarySearchTree()
        self._restar_arboles_recursive(self.__root, other_tree.__root, result_tree)
        return result_tree

    def _restar_arboles_recursive(self, node1, node2, result_tree):
        stack1 = []
        stack2 = []
        current1 = node1
        current2 = node2

        while current1 or stack1 or current2 or stack2:
            while current1:
                stack1.append(current1)
                current1 = current1.left
            while current2:
                stack2.append(current2)
                current2 = current2.left

            if stack1:
                current1 = stack1.pop()
            if stack2:
                current2 = stack2.pop()

            if current1 and current2:
                if current1.degree == current2.degree:
                    print("Restando coeficientes de x^" + str(current1.degree))
                    result_node = result_tree.search(current1.degree)
                    if result_node:
                        result_node.coef += current1.coef
                        result_node.coef += current2.coef
                    else:
                        result_tree.insert(current1.degree, current1.coef - current2.coef)
                    current1 = current1.right
                    current2 = current2.right
                elif current1.degree < current2.degree:
                    result_tree.insert(current1.degree, current1.coef)
                    current1 = current1.right
                else:
                    result_tree.insert(current2.degree, current2.coef)
                    current2 = current2.right
            elif current1:
                result_tree.insert(current1.degree, current1.coef)
                current1 = current1.right
            elif current2:
                result_tree.insert(current2.degree, current2.coef)
                current2 = current2.right

        return result_tree

    def search(self, degree):
        return self._search_recursive(self.__root, degree)

    def _search_recursive(self, node, degree):
        if not node:
            return None
        if degree == node.degree:
            return node
        elif degree < node.degree:
            return self._search_recursive(node.left, degree)
        else:
            return self._search_recursive(node.right, degree)
        
    def evaluate(self, x):
        print("Iniciando evaluacion del polinomio...")
        return self._evaluate_recursive(self.__root, x)

    def _evaluate_recursive(self, node, x):
        if not node:
            return 0
        else:
            result = node.coef * (x ** node.degree)
            print(f"Evaluando termino {node.coef}x^{node.degree}: {node.coef} * ({x}^{node.degree}) = {result}")
            result += self._evaluate_recursive(node.left, x)
            result += self._evaluate_recursive(node.right, x)
            return result