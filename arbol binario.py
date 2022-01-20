class arbol:

    class root:
        def __init__(self, valor):
            self.valor = valor
            self._izquierdo = None
            self._derecho = None

    __slots__ = ['_root','_tamanio']

    def __init__(self):
        self._root = None
        self._tamanio = 0

    def insertar(self, valor): # Método para insertar un valor en el árbol
        if self._root is None:
            self._root = self.root(valor)
            self._tamanio += 1
        else:
            self._insertar(self._root, valor)

    def _insertar(self, nodo, valor): # Método para insertar un valor en el árbol
        if valor < nodo.valor:
            if nodo._izquierdo is None:
                nodo._izquierdo = self.root(valor)
                self._tamanio += 1
            else:
                self._insertar(nodo._izquierdo, valor)
        else:
            if nodo._derecho is None:
                nodo._derecho = self.root(valor)
                self._tamanio += 1
            else:
                self._insertar(nodo._derecho, valor)

    def mostrar(self): # Método para mostrar el árbol
        if self._root is None:
            print('arbol vacio')
        else:
            self._mostrar(self._root)

    def _mostrar(self, nodo): # Método para mostrar el árbol
        if nodo is not None:
            self._mostrar(nodo._izquierdo)
            print(nodo.valor)
            self._mostrar(nodo._derecho)

if __name__ == '__main__':
    arbol = arbol()
    arbol.insertar(10)
    arbol.insertar(5)

    arbol.mostrar()