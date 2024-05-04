from Estructuras.node import Node
from typing import  Generic, Optional, TypeVar
T = TypeVar("T")

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, degree, coef):
        if not self.root:
            self.root = Node(degree, coef)
        else:
            self._insert_recursive(self.root, degree, coef)

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
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, node):
        if node:
            self._print_in_order(node.left)
            print(f"{node.coef}x^{node.degree}", end=' + ')
            self._print_in_order(node.right)