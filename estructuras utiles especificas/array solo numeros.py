from dataclasses import dataclass
from typing import Any, Union

class pila():

    __slots__ = 'numeros', "_tamanio", "_suma", "_promedio" # atributos de la clase

    def __init__(self):
        self.numeros = []       # lista vacia
        self._tamanio = 0       # tamanio de la pila
        self._suma =  0         # suma de la pila
        self._promedio = 0      # promedio de la pila

# funciones de insercion
    def insertar(self, numero) -> None:
        if isinstance(numero, int):
            self.numeros.append(numero) # agrega el numero a la lista
            self._tamanio += 1 # aumenta el tamanio de la lista
            self._suma += numero # aumenta la suma de la lista
            self._promedio = self._suma / self._tamanio # calcula el promedio de la lista
        else:
            raise TypeError("El tipo de dato no es valido")

    def insertar_en_posicion(self, numero, posicion) -> None:
        if isinstance(numero, int): # si el numero es un entero
            self.numeros.insert(posicion, numero) # inserta el numero en la posicion
            self._tamanio += 1 # aumenta el tamanio de la lista
            self._suma += numero # aumenta la suma de la lista
            self._promedio = self._suma / self._tamanio # calcula el promedio de la lista
        else:
            raise TypeError("El tipo de dato no es valido")
# funciones de eliminacion
    def eliminar(self) -> None: # elimina el ultimo elemento de la pila
        if self._tamanio == 0: # si la lista esta vacia
            raise ValueError("La pila esta vacia") # se lanza una excepcion
        else:
            self.numeros.pop() # se elimina el ultimo elemento de la lista
    
    def __delitem__(self, posicion) -> None: # eliminar elemento de la pila
        del self.numeros[posicion]

    def eliminar_duplicados(self) -> None: # elimina los duplicados de la pila
        self.numeros = list(set(self.numeros)) # elimina los duplicados de la lista

# funciones de ordenamiento
    def ordenare_mayor_menor(self) -> None: # ordena de mayor a menor
        self.numeros.sort(reverse=True) 

    def ordenar_mayor_menor(self) -> None: # ordena de mayor a menor
        self.numeros.sort(reverse=True)

# funciones busqueda
    def busqueda_binaria(self, numero) -> bool: # busqueda binaria
        nueva_lista = sorted(self.numeros) # ordena la lista
        longitud = self._tamanio # tamanio de la lista

        if longitud == 0: # si la lista esta vacia
            return False # retorna falso
        while longitud > 1: # mientras la longitud sea mayor a 1
            mitad = longitud // 2 # divide la longitud entre 2
            if nueva_lista[mitad] == numero: # si el numero es igual al numero que se busca
                return True # retorna verdadero
            elif nueva_lista[mitad] > numero: # si el numero es mayor al numero que se busca
                longitud = mitad # la longitud se iguala a la mitad
            else: # si el numero es menor al numero que se busca
                longitud = longitud - mitad # la longitud se iguala a la longitud menos la mitad

        return False  # retorna falso
# funciones utiles
    def suma(self) -> int: # suma de la pila
        return self._suma
    
    def promedio(self) -> float: # promedio de la pila
        return self._promedio

    def tamanio(self) -> int: # tamanio de la pila
        return self._tamanio

# funciones python
    def __repr__(self) -> str: # representacion de la pila
        return str(self.numeros)
    
    def __len__(self) -> int: # longitud de la pila
        return len(self.numeros)

    def __eq__(self, other) -> bool:
        return self.numeros == other.numeros