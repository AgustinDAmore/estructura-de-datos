from dataclasses import dataclass
from typing import Any, Union

class pila():

    __slots__ = 'items', "_tamanio"

    def __init__(self):
        self.items = []
        self._tamanio = 0

    def apilar(self, x):
        self.items.append(x)
        self._tamanio += 1

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("La pila esta vacia")
        self._tamanio -= 1
        return self.items.pop()

    def esta_vacia(self):
        return self._tamanio == 0

    def tamanio(self):
        return self._tamanio

    def ver_tope(self):
        return self.items[-1]

    def copiar(self):
        nuevapila = pila()
        while not self.esta_vacia():
            nuevapila.apilar(self.desapilar())
        return nuevapila
# funciones python
    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return str(self.items)
    
    def __len__(self):
        return len(self.items)
        
# Pruebas
if __name__ == "__main__":
    pila   = pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)

    print(pila)
    print(pila.tamanio())
    print(pila.ver_tope())

    print(pila.desapilar())
    print(pila.desapilar())
    print(pila.desapilar())

    print(pila.esta_vacia())