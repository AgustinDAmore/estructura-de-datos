class grafo:
    def __init__(self, n) -> None: # Constructor
        self.n = n # Cantidad de nodos
        self.matriz = [[0] * n for i in range(n)] # Matriz de adyacencia
        self.visitado = [False] * n # Matriz de visitados

    def agregar_arista(self, u, v) -> None: # Agrega una arista
        self.matriz[u][v] = 1 # Agrega una arista
        self.matriz[v][u] = 1 # Agrega una arista
    
    def agregar_arista(self, u, v, peso) -> None:
        self.agregar_arista_peso(u, v, peso)

    def agregar_arista_peso(self, u, v, peso) -> None: # Agrega una arista con peso 
        self.matriz[u][v] = peso # Agrega una arista
        self.matriz[v][u] = peso # Agrega una arista


    def imprimir(self) -> None: # Imprime el grafo
        for i in range(self.n): # Recorre las filas 
            for j in range(self.n): # Recorre las columnas
                print(self.matriz[i][j], end=' ') # Imprime el peso
            print() # Salto de linea

    def busqueda_en_profundidad_DFS(self, u) -> int: # Busqueda en profundidad
        self.visitado[u] = True # Marca el nodo como visitado
        print(u, end=' ') # Imprime el nodo
        for i in range(self.n): # Recorre las filas
            if self.matriz[u][i] == 1 and self.visitado[i] == False: # Si hay una arista y no fue visitado
                self.busqueda_en_profundidad_DFS(i) # Busca el nodo

    def busqueda_primero_en_amplitud_BFS(self, u) -> int: # Busqueda en amplitud
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        self.visitado[u] = True # Marca el nodo como visitado
        while len(fila) > 0: # Mientras la fila no este vacia
            u = fila.pop(0) # Extrae el nodo
            print(u, end=' ') # Imprime el nodo
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and self.visitado[i] == False: # Si hay una arista y no fue visitado
                    fila.append(i)  # Agrega el nodo
                    self.visitado[i] = True # Marca el nodo como visitado
    
    def busqueda_en_profundidad_recursiva_DFS(self, u, visitado): # Busqueda en profundidad
        visitado[u] = True # Marca el nodo como visitado
        print(u, end=' ')  # Imprime el nodo
        for i in range(self.n): # Recorre las filas
            if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                self.busqueda_en_profundidad_recursiva_DFS(i, visitado) # Busca el nodo
    
    def busqueda_en_profundidad_recursiva_DFS_iterativa(self, u): # Busqueda en profundidad
        visitado = [False] * self.n # Matriz de visitados
        self.busqueda_en_profundidad_recursiva_DFS(u, visitado) # Busca el nodo

    def profundidad(self, u) -> int: # Profundidad del nodo
        visitado = [False] * self.n # Matriz de visitados
        profundidad = 0 # Profundidad
        self.busqueda_en_profundidad_recursiva_DFS(u, visitado) # Busca el nodo
        for i in range(self.n): # Recorre las filas
            if visitado[i] == True: # Si fue visitado
                profundidad += 1 # Aumenta la profundidad
        return profundidad # Retorna la profundidad

    def anchura(self, u) -> int: # Profundidad del nodo
        visitado = [False] * self.n # Matriz de visitados
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        visitado[u] = True # Marca el nodo como visitado
        profundidad = 0 # Profundidad
        while len(fila) > 0: # Mientras la fila no este vacia
            u = fila.pop(0) # Extrae el nodo
            profundidad += 1 # Aumenta la profundidad
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                    fila.append(i) # Agrega el nodo
                    visitado[i] = True # Marca el nodo como visitado
        return profundidad # Retorna la profundidad

    def peso(self, u, v) -> int: # Peso del nodo
        return self.matriz[u][v] # Retorna el peso

    def distancia_minima(self, u, v) -> int: # Distancia minima del nodo
        visitado = [False] * self.n # Matriz de visitados
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        visitado[u] = True # Marca el nodo como visitado
        distancia = [float('inf')] * self.n # Matriz de distancias
        distancia[u] = 0 # Distancia del nodo
        while len(fila) > 0: # Mientras la fila no este vacia 
            u = fila.pop(0) # Extrae el nodo
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                    distancia[i] = min(distancia[i], distancia[u] + self.peso(u, i)) # Actualiza la distancia
                    fila.append(i) # Agrega el nodo
                    visitado[i] = True # Marca el nodo como visitado
        return distancia[v] # Retorna la distancia
    
    def camino_minimo(self, u, v) -> int: # Camino minimo del nodo
        visitado = [False] * self.n # Matriz de visitados
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        visitado[u] = True # Marca el nodo como visitado
        distancia = [float('inf')] * self.n # Matriz de distancias
        distancia[u] = 0 # Distancia del nodo
        padre = [-1] * self.n # Matriz de padres
        while len(fila) > 0: # Mientras la fila no este vacia
            u = fila.pop(0) # Extrae el nodo
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                    if distancia[i] > distancia[u] + self.peso(u, i): # Si la distancia es mayor
                        distancia[i] = distancia[u] + self.peso(u, i) # Actualiza la distancia
                        padre[i] = u # Actualiza el padre
                    fila.append(i) # Agrega el nodo
                    visitado[i] = True # Marca el nodo como visitado
        return distancia[v], padre # Retorna la distancia y el padre

    def distancia_maxima(self, u, v) -> int: # Distancia maxima del nodo
        visitado = [False] * self.n # Matriz de visitados
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        visitado[u] = True # Marca el nodo como visitado
        distancia = [float('inf')] * self.n # Matriz de distancias
        distancia[u] = 0 # Distancia del nodo
        while len(fila) > 0: # Mientras la fila no este vacia
            u = fila.pop(0) # Extrae el nodo
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                    distancia[i] = max(distancia[i], distancia[u] + self.peso(u, i)) # Actualiza la distancia
                    fila.append(i) # Agrega el nodo
                    visitado[i] = True # Marca el nodo como visitado
        return distancia[v] # Retorna la distancia
    
    def camino_maximo(self, u, v) -> int: # Camino maximo del nodo
        visitado = [False] * self.n # Matriz de visitados
        fila = [] # Fila de nodos
        fila.append(u) # Agrega el nodo
        visitado[u] = True # Marca el nodo como visitado
        distancia = [float('inf')] * self.n # Matriz de distancias
        distancia[u] = 0 # Distancia del nodo
        padre = [-1] * self.n # Matriz de padres
        while len(fila) > 0: # Mientras la fila no este vacia
            u = fila.pop(0) # Extrae el nodo
            for i in range(self.n): # Recorre las filas
                if self.matriz[u][i] == 1 and visitado[i] == False: # Si hay una arista y no fue visitado
                    if distancia[i] < distancia[u] + self.peso(u, i): # Si la distancia es mayor
                        distancia[i] = distancia[u] + self.peso(u, i) # Actualiza la distancia
                        padre[i] = u # Actualiza el padre
                    fila.append(i) # Agrega el nodo
                    visitado[i] = True # Marca el nodo como visitado
        return distancia[v], padre  # Retorna la distancia y el padre

    def __len__(self) -> int: # Retorna la cantidad de nodos
        return len(self.matriz) # Retorna la cantidad de nodos

    def __eq__(self, __o: object) -> bool: # Compara si son iguales
        if isinstance(__o, grafo): # Si es un grafo
            return self.matriz == __o.matriz # Retorna si son iguales
        return False # Retorna falso

    def __str__(self) -> str: # Retorna la representacion del grafo
        return str(self.matriz) # Retorna la representacion del grafo
 
    def __repr__(self) -> str: # Retorna la representacion del grafo
        return str(self.matriz) # Retorna la representacion del grafo

if __name__ == "__main__":
    g = grafo(5) # Crea un grafo de 5 nodos
    g.agregar_arista_peso(0, 1, 1) # Agrega la arista 0-1
    g.agregar_arista_peso(0, 2, 2) # Agrega la arista 0-2
    g.agregar_arista_peso(1, 2, 3) # Agrega la arista 1-2
    g.agregar_arista_peso(1, 3, 4) # Agrega la arista 1-3
    g.agregar_arista_peso(2, 3, 5) # Agrega la arista 2-3
    g.agregar_arista_peso(2, 4, 6) # Agrega la arista 2-4
    g.agregar_arista(3, 4, 7) # Agrega la arista 3-4
    print(g) # Imprime el grafo
    print(g.peso(0, 1)) # Imprime el peso de la arista 0-1
    print(g.peso(0, 2)) # Imprime el peso de la arista 0-2
    print(g.peso(1, 2)) # Imprime el peso de la arista 1-2
    print(g.peso(1, 3)) # Imprime el peso de la arista 1-3
    print(g.peso(2, 3)) # Imprime el peso de la arista 2-3
    print(g.peso(2, 4)) # Imprime el peso de la arista 2-4
    print(g.peso(3, 4)) # Imprime el peso de la arista 3-4
    print(g.peso(4, 0)) # Imprime el peso de la arista 4-0
    print(g.peso(4, 1)) # Imprime el peso de la arista 4-1
    print(g.peso(4, 2)) # Imprime el peso de la arista 4-2
    print(g.peso(4, 3)) # Imprime el peso