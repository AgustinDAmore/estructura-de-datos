class ArbolBinarioAVL: # Clase para el arbol binario
    class raiz: # Clase para el nodo raiz
        def __init__(self, dato):   # Constructor
            self.dato = dato    # Dato del nodo
            self.izquierda = None   # Nodo izquierdo
            self.derecha = None  # Nodo derecho
            self.altura = 0 # Altura del nodo
        
        def __eq__(self, other):    # Compara dos nodos
            return self.dato == other.dato  # Retorna True si son iguales
        
        def izquierda(self):    # Retorna el nodo izquierdo
            return self.izquierda   # Retorna el nodo izquierdo
        
        def derecha(self):  # Retorna el nodo derecho
            return self.derecha  # Retorna el nodo derecho
        
        def altura(self):   # Retorna la altura del nodo
            return self.altura  # Retorna la altura del nodo

    class Nodo: # Clase para el nodo
        def __init__(self, dato):   # Constructor
            self.dato = dato    # Dato del nodo
            self.izquierda = None   # Nodo izquierdo
            self.derecha = None # Nodo derecho
            self.peso = 1   # Peso del nodo

        def izquierda(self):    # Retorna el nodo izquierdo
            return self.izquierda   # Retorna el nodo izquierdo
        
        def derecha(self):  # Retorna el nodo derecho
            return self.derecha # Retorna el nodo derecho

        def peso(self):  # Retorna el peso del nodo
            return self.peso    # Retorna el peso del nodo

        def __str__(self):  # Retorna el dato del nodo
            return str(self.dato)   # Retorna el dato del nodo
        
        def __repr__(self): # Retorna el dato del nodo
            return str(self.dato)   # Retorna el dato del nodo

    def __init__(self): # Constructor
        self.raiz = None    # Raiz del arbol

# funciones insertar

    def insertar(self, dato):   # Inserta un nodo en el arbol
        self.raiz = self.insertar_aux(self.raiz, dato)  # Inserta el nodo en el arbol
    
    def insertar_aux(self, nodo, dato):  # Inserta un nodo en el arbol
        if nodo == None:    # Si el nodo es nulo
            nodo = self.Nodo(dato)  # Crea el nodo
        elif dato < nodo.dato:  # Si el dato es menor que el nodo
            nodo.izquierda = self.insertar_aux(nodo.izquierda, dato)    # Inserta el nodo en el arbol
            if self.altura(nodo.izquierda) - self.altura(nodo.derecha) == 2:  # Si la diferencia de alturas es 2
                if dato < nodo.izquierda.dato:  # Si el dato es menor que el nodo izquierdo
                    nodo = self.rotacion_derecha(nodo)  # Rota el nodo derecho
                else:   # Si el dato es mayor que el nodo izquierdo
                    nodo = self.rotacion_doble_derecha(nodo)    # Rota el nodo doble derecho
        elif dato > nodo.dato:  # Si el dato es mayor que el nodo
            nodo.derecha = self.insertar_aux(nodo.derecha, dato)    # Inserta el nodo en el arbol
            if self.altura(nodo.derecha) - self.altura(nodo.izquierda) == 2:    # Si la diferencia de alturas es 2
                if dato > nodo.derecha.dato:    # Si el dato es mayor que el nodo derecho
                    nodo = self.rotacion_izquierda(nodo)    # Rota el nodo izquierdo
                else:   # Si el dato es menor que el nodo derecho
                    nodo = self.rotacion_doble_izquierda(nodo)  # Rota el nodo doble izquierdo
        nodo.peso = self.altura(nodo.izquierda) + self.altura(nodo.derecha) + 1 # Actualiza el peso del nodo
        return nodo # Retorna el nodo raiz

# funciones rotar

    def rotacion_derecha(self, nodo):   # Rota el nodo derecho
        aux = nodo.izquierda    # Guarda el nodo izquierdo
        nodo.izquierda = aux.derecha    # Cambia el nodo izquierdo por el derecho
        aux.derecha = nodo  # Cambia el nodo derecho por el nodo izquierdo
        nodo.peso = self.altura(nodo.izquierda) + self.altura(nodo.derecha) + 1 # Actualiza el peso del nodo
        aux.peso = self.altura(aux.izquierda) + self.altura(aux.derecha) + 1    # Actualiza el peso del nodo
        return aux  # Retorna el nodo izquierdo

    def rotacion_izquierda(self, nodo):  # Rota el nodo izquierdo
        aux = nodo.derecha  # Guarda el nodo derecho
        nodo.derecha = aux.izquierda    # Cambia el nodo derecho por el izquierdo
        aux.izquierda = nodo    # Cambia el nodo izquierdo por el nodo derecho
        nodo.peso = self.altura(nodo.izquierda) + self.altura(nodo.derecha) + 1 # Actualiza el peso del nodo
        aux.peso = self.altura(aux.izquierda) + self.altura(aux.derecha) + 1    # Actualiza el peso del nodo
        return aux  # Retorna el nodo derecho

    def rotacion_doble_derecha(self, nodo): # Rota el nodo doble derecho
        nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)    # Rota el nodo izquierdo
        return self.rotacion_derecha(nodo)  # Rota el nodo derecho

    def rotacion_doble_izquierda(self, nodo):   # Rota el nodo doble izquierdo
        nodo.derecha = self.rotacion_derecha(nodo.derecha)  # Rota el nodo derecho
        return self.rotacion_izquierda(nodo)  # Rota el nodo izquierdo

# funciones eliminar
    def eliminar(self, dato):   # Elimina el nodo
        self.raiz = self.eliminar_aux(self.raiz, dato)  # Elimina el nodo

    def eliminar_aux(self, nodo, dato):  # Elimina el nodo
        if nodo == None:    # Si el nodo es nulo
            return None  # Retorna None
        elif dato < nodo.dato:  # Si el dato es menor que el nodo
            nodo.izquierda = self.eliminar_aux(nodo.izquierda, dato)    # Elimina el nodo
            if self.altura(nodo.derecha) - self.altura(nodo.izquierda) == 2:    # Si la diferencia de alturas es 2
                if self.altura(nodo.derecha.derecha) > self.altura(nodo.derecha.izquierda):   # Si la altura del nodo derecho derecho es mayor que la altura del nodo derecho izquierdo
                    nodo = self.rotacion_derecha(nodo)  # Rota el nodo derecho
                else:   # Si la altura del nodo derecho derecho es menor que la altura del nodo derecho izquierdo
                    nodo = self.rotacion_doble_derecha(nodo)    # Rota el nodo doble derecho
        elif dato > nodo.dato:  # Si el dato es mayor que el nodo
            nodo.derecha = self.eliminar_aux(nodo.derecha, dato)    # Elimina el nodo
            if self.altura(nodo.derecha) - self.altura(nodo.izquierda) == 2:    # Si la diferencia de alturas es 2
                if self.altura(nodo.izquierda.izquierda) > self.altura(nodo.izquierda.derecha):  # Si la altura del nodo izquierdo izquierdo es mayor que la altura del nodo izquierdo derecho
                    nodo = self.rotacion_izquierda(nodo)    # Rota el nodo izquierdo
                else:   # Si la altura del nodo izquierdo izquierdo es menor que la altura del nodo izquierdo derecho
                    nodo = self.rotacion_doble_izquierda(nodo)  # Rota el nodo doble izquierdo
        else:   # Si el dato es igual al nodo
            if nodo.izquierda == None and nodo.derecha == None:   # Si el nodo es nulo
                nodo = None   # Retorna None
            elif nodo.izquierda == None:    # Si el nodo izquierdo es nulo
                nodo = nodo.derecha  # Retorna el nodo derecho
            elif nodo.derecha == None:  # Si el nodo derecho es nulo
                nodo = nodo.izquierda   # Retorna el nodo izquierdo
            else:   # Si el nodo tiene dos hijos
                aux = self.minimo(nodo.derecha)   # Retorna el nodo minimo
                nodo.dato = aux.dato    # Cambia el dato del nodo
                nodo.derecha = self.eliminar_aux(nodo.derecha, aux.dato)    # Elimina el nodo
        if nodo != None:    # Si el nodo no es nulo
            nodo.peso = self.altura(nodo.izquierda) + self.altura(nodo.derecha) + 1 # Actualiza el peso del nodo

# funciones buscar

    def buscar(self, dato):   # Retorna el nodo si lo encuentra
        return self.buscar_aux(self.raiz, dato) # Retorna el nodo si lo encuentra
    
    def buscar_aux(self, nodo, dato):   # Retorna el nodo si lo encuentra
        if nodo == None:    # Si el nodo es nulo
            return False    # Retorna False
        elif dato == nodo.dato:   # Si el dato es igual al nodo
            return True   # Retorna True
        elif dato < nodo.dato:  # Si el dato es menor que el nodo
            return self.buscar_aux(nodo.izquierda, dato)    # Retorna el nodo si lo encuentra
        else:   # Si el dato es mayor que el nodo
            return self.buscar_aux(nodo.derecha, dato)  # Retorna el nodo si lo encuentra

    def buscar_menor(self, nodo):   # Retorna el nodo minimo
        if nodo.izquierda == None:  # Si el nodo izquierdo es nulo
            return nodo # Retorna el nodo
        else:   # Si el nodo izquierdo no es nulo
            return self.buscar_menor(nodo.izquierda)    # Retorna el nodo minimo
    
    def buscar_mayor(self, nodo):   # Retorna el nodo maximo
        if nodo.derecha == None:    # Si el nodo derecho es nulo
            return nodo # Retorna el nodo
        else:   # Si el nodo derecho no es nulo
            return self.buscar_mayor(nodo.derecha)  # Retorna el nodo maximo

    def buscar_padre(self, nodo, dato):  # Retorna el nodo padre
        if nodo.dato == dato:   # Si el nodo es igual al dato
            return None # Retorna None
        elif dato < nodo.dato:  # Si el dato es menor que el nodo
            if nodo.izquierda.dato == dato: # Si el nodo izquierdo es igual al dato
                return nodo # Retorna el nodo
            else:   # Si el nodo izquierdo no es igual al dato
                return self.buscar_padre(nodo.izquierda, dato)  # Retorna el nodo padre
        else:   # Si el dato es mayor que el nodo
            if nodo.derecha.dato == dato:   # Si el nodo derecho es igual al dato
                return nodo # Retorna el nodo
            else:   # Si el nodo derecho no es igual al dato
                return self.buscar_padre(nodo.derecha, dato)    # Retorna el nodo padre

    def buscar_hijo_izquierdo(self, nodo):  # Retorna el nodo izquierdo
        if nodo.izquierda == None:  # Si el nodo izquierdo es nulo
            return None # Retorna None
        else:   # Si el nodo izquierdo no es nulo
            return nodo.izquierda   # Retorna el nodo izquierdo

    def buscar_hijo_derecho(self, nodo):    # Retorna el nodo derecho
        if nodo.derecha == None:    # Si el nodo derecho es nulo
            return None # Retorna None
        else:   # Si el nodo derecho no es nulo
            return nodo.derecha  # Retorna el nodo derecho

    def buscar_hermano_izquierdo(self, nodo):   # Retorna el nodo hermano izquierdo
        if nodo.padre == None:  # Si el nodo padre es nulo
            return None # Retorna None
        elif nodo.padre.izquierda == nodo:  # Si el nodo padre es igual al nodo
            return nodo.padre.derecha   # Retorna el nodo derecho
        else:   # Si el nodo padre no es igual al nodo
            return nodo.padre.izquierda # Retorna el nodo izquierdo

    def buscar_hermano_derecho(self, nodo):   # Retorna el nodo hermano derecho
        if nodo.padre == None:  # Si el nodo padre es nulo
            return None # Retorna None
        elif nodo.padre.derecha == nodo:    # Si el nodo padre es igual al nodo
            return nodo.padre.izquierda  # Retorna el nodo izquierdo
        else:   # Si el nodo padre no es igual al nodo
            return nodo.padre.derecha   # Retorna el nodo derecho

# funciones orden

    def inorden(self):  # Retorna el arbol en inorden
        self.inorden_aux(self.raiz) # Retorna el arbol en inorden

    def inorden_aux(self, nodo):    # Retorna el arbol en inorden
        if nodo != None:    # Si el nodo no es nulo
            self.inorden_aux(nodo.izquierda)    # Retorna el arbol en inorden
            print(nodo.dato)    # Imprime el dato del nodo
            self.inorden_aux(nodo.derecha)  # Retorna el arbol en inorden

    def preorden(self): # Retorna el arbol en preorden
        self.preorden_aux(self.raiz)    # Retorna el arbol en preorden

    def preorden_aux(self, nodo):   # Retorna el arbol en preorden
        if nodo != None:    # Si el nodo no es nulo
            print(nodo.dato)    # Imprime el dato del nodo
            self.preorden_aux(nodo.izquierda)   # Retorna el arbol en preorden
            self.preorden_aux(nodo.derecha) # Retorna el arbol en preorden

    def postorden(self):    # Retorna el arbol en postorden
        self.postorden_aux(self.raiz)   # Retorna el arbol en postorden

    def postorden_aux(self, nodo):  # Retorna el arbol en postorden
        if nodo != None:   # Si el nodo no es nulo
            self.postorden_aux(nodo.izquierda)  # Retorna el arbol en postorden
            self.postorden_aux(nodo.derecha)    # Retorna el arbol en postorden
            print(nodo.dato)    # Imprime el dato del nodo

# funciones otras
            
    def minimo(self, nodo):  # Retorna el nodo minimo
        while nodo.izquierda != None:   # Mientras el nodo izquierdo no sea nulo
            nodo = nodo.izquierda   # Retorna el nodo izquierdo
        return nodo  # Retorna el nodo

    def altura(self, nodo): # Retorna la altura del nodo
        if nodo == None:    # Si el nodo es nulo
            return -1   # Retorna -1
        else:   # Si el nodo no es nulo
            return nodo.peso    # Retorna el peso del nodo

# funciones python
    def __str__(self) -> str:  # Retorna un string con el arbol
        return str(self.inorden())  # Retorna un string con el arbol

    def __repr__(self) -> str: # Retorna un string con el arbol
        return str(self.inorden())  # Retorna un string con el arbol
    
    def __len__(self) -> int:   # Retorna el largo del arbol
        return self.tamanio(self.raiz)  # Retorna el largo del arbol

    def tamanio(self, nodo) -> int:    # Retorna el largo del arbol
        if nodo == None:    # Si el nodo es nulo
            return 0    # Retorna 0
        else:   # Si el nodo no es nulo
            return self.tamanio(nodo.izquierda) + 1 + self.tamanio(nodo.derecha)    # Retorna el largo del arbol
    
    def altura(self, nodo) -> int: # Retorna la altura del arbol
        if nodo == None:    # Si el nodo es nulo
            return -1   # Retorna -1
        else:   # Si el nodo no es nulo
            return nodo.peso    # Retorna la altura del arbol
    
if __name__ == "__main__": # Para que no se ejecute cuando importa el archivo
    arbol = ArbolBinarioAVL()
    arbol.insertar('a')
    arbol.insertar('A')
    arbol.insertar('b')
    arbol.insertar('B')
    arbol.insertar('c')
    arbol.insertar('C')