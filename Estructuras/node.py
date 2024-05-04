from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, degree: T, coef: T):
        self._degree = degree
        self._coef = coef
        self._left: Optional['Node[T]'] = None
        self._right: Optional['Node[T]'] = None

    @property
    def degree(self) -> T:
        """Getter para el grado del término."""
        return self._degree

    @degree.setter
    def degree(self, value: T):
        """Setter para el grado del término."""
        self._degree = value

    @property
    def coef(self) -> T:
        """Getter para el coeficiente del término."""
        return self._coef

    @coef.setter
    def coef(self, value: T):
        """Setter para el coeficiente del término."""
        self._coef = value

    @property
    def left(self) -> Optional['Node[T]']:
        """Getter para el hijo izquierdo del nodo."""
        return self._left

    @left.setter
    def left(self, value: Optional['Node[T]']):
        """Setter para el hijo izquierdo del nodo."""
        self._left = value

    @property
    def right(self) -> Optional['Node[T]']:
        """Getter para el hijo derecho del nodo."""
        return self._right

    @right.setter
    def right(self, value: Optional['Node[T]']):
        """Setter para el hijo derecho del nodo."""
        self._right = value





