class lista_enlazada:

    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
    
    __slots__ = '__cabeza', '__cola', '__tamanio'

    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0

    def insertar_inicio(self, dato):
        nuevo = self.Nodo(dato)
        if self.__tamanio == 0:
            self.__cabeza = nuevo
            self.__cola = nuevo
        else:
            nuevo.siguiente = self.__cabeza
            self.__cabeza = nuevo
        self.__tamanio += 1
    
    def insertar_final(self, dato):
        nuevo = self.Nodo(dato)
        if self.__tamanio == 0:
            self.__cabeza = nuevo
            self.__cola = nuevo
        else:
            self.__cola.siguiente = nuevo
            self.__cola = nuevo
        self.__tamanio += 1
    
    def insertar_posicion(self, posicion, dato):
        if posicion > self.__tamanio:
            raise IndexError('Posicion invalida')
        if posicion == 0:
            self.insertar_inicio(dato)
        elif posicion == self.__tamanio:
            self.insertar_final(dato)
        else:
            nuevo = self.Nodo(dato)
            aux = self.__cabeza
            for i in range(posicion - 1):
                aux = aux.siguiente
            nuevo.siguiente = aux.siguiente
            aux.siguiente = nuevo
            self.__tamanio += 1
    
    def eliminar_inicio(self):
        if self.__tamanio == 0:
            raise IndexError('Lista vacia')
        else:
            aux = self.__cabeza
            self.__cabeza = aux.siguiente
            self.__tamanio -= 1
            if self.__tamanio == 0:
                self.__cola = None
            return aux.dato
    
    def eliminar_final(self):
        if self.__tamanio == 0:
            raise IndexError('Lista vacia')
        else:
            aux = self.__cabeza
            if self.__tamanio == 1:
                self.__cabeza = None
                self.__cola = None
            else:
                while aux.siguiente != self.__cola:
                    aux = aux.siguiente
                aux.siguiente = None
                self.__cola = aux
            self.__tamanio -= 1
    
    def eliminar_posicion(self, posicion):
        if posicion > self.__tamanio:
            raise IndexError('Posicion invalida')
        if posicion == 0:
            self.eliminar_inicio()
        elif posicion == self.__tamanio:
            self.eliminar_final()
        else:
            aux = self.__cabeza
            for i in range(posicion - 1):
                aux = aux.siguiente
            aux.siguiente = aux.siguiente.siguiente
            self.__tamanio -= 1

    def iterador(self):
        aux = self.__cabeza
        while aux != None:
            yield aux.dato
            aux = aux.siguiente

    def __iter__(self):
        return self.iterador()

    def __len__(self):
        return self.__tamanio
    
    def __str__(self):
        if self.__tamanio == 0:
            return 'Lista vacia'
        else:
            aux = self.__cabeza
            cadena = 'inicio -> '
            while aux != None:
                cadena += str(aux.dato) + ' -> '
                aux = aux.siguiente
            return cadena + 'fin'

if __name__ == '__main__':
    lista = lista_enlazada()
    lista.insertar_inicio(1)
    lista.insertar_inicio(2)
    lista.insertar_inicio(3)
    lista.insertar_inicio(4)
    lista.insertar_inicio(5)
    print(lista)
    lista.eliminar_final()
    print(lista)
    lista.eliminar_inicio()
    print(lista)
    lista.insertar_final(5)
    print(lista)
    