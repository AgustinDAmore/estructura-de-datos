from dataclasses import dataclass
from typing import Any, Union

class queue():
    __slots__ = ('_elements',"_size","_type")

    def __init__(self,element) -> None:
        self._elements = [element]
        self._size = 0
        self._type = type(element)


    def encolar(self, elemento: Any) -> None:
        if type(elemento) == self._type:
            self._elements.append(elemento)
            self._size += 1
        else:
            raise TypeError("the type of the element is not the same as the type of the queue")

    def desencolar(self) -> Any:
        if self._size == 0:
            raise IndexError("the line is empty")
        self._size -= 1
        return self._elements.pop()

    def is_empty(self) -> bool:
        return self._size == 0

    def en(self,elemento: Any) -> bool:
        return elemento in self._elements

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return str(self._elements)