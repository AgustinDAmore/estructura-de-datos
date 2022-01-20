from dataclasses import dataclass
from typing import Any, Union

class lista():
    __slots__ = ('__elementos',"__tamanio")
    def __init__(self) -> None:
        self.__elementos = []
        self.__tamanio = 0

    def encolar(self, elemento: Any) -> None:
        self.__elementos.insert(0,elemento)
        self.__tamanio += 1

    def desencolar(self) -> Any:
        if self.__tamanio == 0:
            raise IndexError("La lista esta vacia")
        self.__tamanio -= 1
        return self.__elementos.pop()

    def esta_vacia(self) -> bool:
        return self.__tamanio == 0

    def en(self,elemento: Any) -> bool:
        return elemento in self.__elementos

    def __len__(self) -> int:
        return self.__tamanio

    def __repr__(self) -> str:
        return str(self.__elementos)