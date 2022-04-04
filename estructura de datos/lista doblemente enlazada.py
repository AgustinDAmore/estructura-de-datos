class lista_doblemente_enlazada:
    class Nodo: # Clase nodo
        def __init__(self, dato): # Constructor
            self.dato = dato # Dato
            self.siguiente = None # Siguiente
            self.anterior = None # Anterior

        def siguiente(self): # Método para obtener el siguiente nodo
            return self.siguiente # Retorna el siguiente nodo

        def anterior(self): # Método para obtener el anterior nodo
            return self.anterior # Retorna el anterior nodo

        def __str__(self): # Método para imprimir el nodo
            return str(self.dato) # Retorna el dato
    
    __slots__ = ['primero', 'ultimo','_tamanio'] # Evita que se creen atributos

    def __init__(self): # Constructor
        self._tamanio = 0 # Tamaño
        self.primero = None # Primero
        self.ultimo = None # Ultimo

    def insertar_final(self, dato): # Método para insertar al final
        nodo = self.Nodo(dato) # Crea un nodo
        if self.primero is None: # Si la lista está vacía
            self.primero = nodo # Primero apunta al nodo
            self.ultimo = nodo
        else: # Si la lista no está vacía
            nodo.anterior = self.ultimo # El nodo anterior apunta al último nodo
            self.ultimo.siguiente = nodo # El último nodo apunta al nodo
            self.ultimo = nodo # El último nodo apunta al nodo
        self._tamanio += 1 # Aumenta el tamaño

    def insertar_inicio(self, dato): # Método para insertar al inicio
        nodo = self.Nodo(dato) # Crea un nodo
        if self.primero is None: # Si la lista está vacía
            self.primero = nodo # Primero apunta al nodo
            self.ultimo = nodo # Ultimo apunta al nodo
        else: # Si la lista no está vacía
            nodo.siguiente = self.primero # El nodo siguiente apunta al primero nodo
            self.primero.anterior = nodo # El primero nodo apunta al nodo
            self.primero = nodo # Primero apunta al nodo
        self._tamanio += 1 # Aumenta el tamaño

    def insertar_posicion(self, posicion, dato): # Método para insertar en una posición
        if posicion < 0 or posicion > self._tamanio: # Si la posición es inválida
            raise IndexError('Posicion invalida') # Lanza una excepción
        if posicion == 0: # Si la posición es 0 
            self.insertar_inicio(dato) # Inserta al inicio
        elif posicion == self._tamanio: # Si la posición es igual al tamaño
            self.insertar_final(dato) # Inserta al final
        else: # Si la posición es mayor a 0 y menor al tamaño
            nodo = self.Nodo(dato) # Crea un nodo
            actual = self.primero # Actual apunta al primero nodo
            for i in range(posicion): # Recorre la lista
                actual = actual.siguiente # Actual apunta al siguiente nodo
            nodo.siguiente = actual # El nodo siguiente apunta al nodo actual
            nodo.anterior = actual.anterior # El nodo anterior apunta al nodo anterior del actual
            actual.anterior.siguiente = nodo # El nodo anterior del actual apunta al nodo
            actual.anterior = nodo # El nodo anterior del actual apunta al nodo
            self._tamanio += 1 # Aumenta el tamaño

    def eliminar_final(self): # Método para eliminar al final
        if self.primero is None: # Si la lista está vacía
            raise IndexError('Lista vacia') # Lanza una excepción
        elif self.primero == self.ultimo: # Si la lista tiene un solo elemento
            self.primero = None # Primero apunta a None
            self.ultimo = None # Ultimo apunta a None
        else:
            self.ultimo = self.ultimo.anterior # El último nodo apunta al nodo anterior
            self.ultimo.siguiente = None # El nodo siguiente del último nodo apunta a None
        self._tamanio -= 1 # Disminuye el tamaño

    def eliminar_inicio(self):  # Método para eliminar al inicio
        if self.primero is None:    # Si la lista está vacía
            raise IndexError('Lista vacia') # Lanza una excepción
        elif self.primero == self.ultimo:   # Si la lista tiene un solo elemento
            self.primero = None # Primero apunta a None
            self.ultimo = None  # Ultimo apunta a None
        else:   # Si la lista tiene más de un elemento
            self.primero = self.primero.siguiente # Primero apunta al siguiente nodo
            self.primero.anterior = None    # El nodo anterior del primero apunta a None
        self._tamanio -= 1  # Disminuye el tamaño

    def eliminar_posicion(self, posicion):  # Método para eliminar en una posición
        if posicion < 0 or posicion > self._tamanio:    # Si la posición es inválida
            raise IndexError('Posicion invalida')   # Lanza una excepción
        if posicion == 0:   # Si la posición es 0
            self.eliminar_inicio()  # Elimina al inicio
        elif posicion == self._tamanio: # Si la posición es igual al tamaño
            self.eliminar_final()   # Elimina al final
        else:   # Si la posición es mayor a 0 y menor al tamaño
            actual = self.primero   # Actual apunta al primero nodo
            for i in range(posicion):   # Recorre la lista
                actual = actual.siguiente   # Actual apunta al siguiente nodo
            actual.anterior.siguiente = actual.siguiente    # El nodo anterior del actual apunta al nodo siguiente del actual
            actual.siguiente.anterior = actual.anterior   # El nodo siguiente del actual apunta al nodo anterior del actual
            self._tamanio -= 1  # Disminuye el tamaño

    def tamanio(self):  # Método para obtener el tamaño
        return self._tamanio    # Retorna el tamaño
    
    def buscar(self, dato): # Método para buscar un elemento
        if self.primero is None:    # Si la lista está vacía
            return False    # Retorna False
        else:
            actual = self.primero   # Actual apunta al primero nodo
            while actual is not None:   # Recorre la lista
                if actual.dato == dato:  # Si el dato del nodo actual es igual al dato
                    return True  # Retorna True
                actual = actual.siguiente   # Actual apunta al siguiente nodo
            return False    # Retorna False

    def buscar_posicion(self, dato):    # Método para buscar un elemento en una posición
        if self.primero is None:    # Si la lista está vacía
            return False    # Retorna False
        else:   # Si la lista no está vacía
            actual = self.primero   # Actual apunta al primero nodo
            posicion = 0    # Posición inicializa en 0
            while actual is not None:   # Recorre la lista
                if actual.dato == dato: # Si el dato del nodo actual es igual al dato
                    return posicion # Retorna la posición
                actual = actual.siguiente   # Actual apunta al siguiente nodo
                posicion += 1   # Aumenta la posición
            return False    # Retorna False
    
    def dato_en_posicion(self, posicion):   # Método para obtener el dato en una posición
        if posicion < 0 or posicion > self._tamanio:    # Si la posición es inválida
            raise IndexError('Posicion invalida')   # Lanza una excepción
        if posicion == 0:   # Si la posición es 0
            return self.primero.dato    # Retorna el dato del primero nodo
        else:   # Si la posición es mayor a 0
            actual = self.primero   # Actual apunta al primero nodo
            for i in range(posicion):   # Recorre la lista
                actual = actual.siguiente   # Actual apunta al siguiente nodo
            return actual.dato  # Retorna el dato del nodo actual

    def __str__(self) -> str:   # Método para imprimir la lista
        if self.primero is None:    # Si la lista está vacía
            return 'Lista vacia'    # Retorna Lista vacia
        else:   # Si la lista no está vacía
            cadena = ''   # Cadena inicializa en vacía
            actual = self.primero   # Actual apunta al primero nodo
            while actual is not None:   # Recorre la lista
                cadena += str(actual) + ' <-> '  # Añade el dato del nodo actual y un <->
                actual = actual.siguiente   # Actual apunta al siguiente nodo
            return cadena   # Retorna la cadena
    
if __name__ == '__main__':  # Si se ejecuta el archivo
    l = lista_doblemente_enlazada()
    l.insertar_final(1)
    l.insertar_inicio(2)
    l.insertar_final(3)
    l.insertar_inicio(4)
    l.insertar_final(5)

    print(l)

    l.insertar_posicion(2, 6)
    print(l)