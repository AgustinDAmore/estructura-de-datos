from dataclasses import dataclass
from typing import Any, Union

class lista():
    __slots__ = ('__elementos',"__tamanio","__tamanio_maximo")
    def __init__(self, tamanio_maximo) -> None:
        self.__elementos = []
        self.__tamanio = -1
        self.__tamanio_maximo = tamanio_maximo

    def encolar(self, elemento) -> None:
        if self.__tamanio < self.__tamanio_maximo:
            self.__elementos.insert(0,elemento)
            self.__tamanio += 1
        else:
            raise ValueError("La lista esta llena")
    
    def tamanio(self) -> int:
        return self.__tamanio

    def set_tamanio_maximo(self, tamanio_maximo) -> None:
        if tamanio_maximo > self.__tamanio:
            self.__tamanio_maximo = tamanio_maximo

    def desencolar(self) -> Any:
        if self.__tamanio > 0:
            self.__tamanio -= 1
            return self.__elementos.pop(0)
        else:
            raise ValueError("La lista esta vacia")

    def esta_vacia(self) -> bool:
        return self.__tamanio == 0

    def en(self,elemento: Any) -> bool:
        return elemento in self.__elementos

    def __len__(self) -> int:
        return self.__tamanio

    def __repr__(self) -> str:
        return str(self.__elementos)