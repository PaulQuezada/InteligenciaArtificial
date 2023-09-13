import random
import time
from collections import deque
visitados = set()
class Nodo:
    # Clase que representa un nodo en el arbol de busqueda
    def __init__(self, tablero=None, padre=None, accion=None):
        self.tablero = tablero
        self.padre = padre
        self.accion = accion
    # Metodo para obtener la posicion del espacio en el tablero
    def obtener_vacio(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == '_':
                    return (i, j)

    def obtener_sucesores(self):
        i, j = self.obtener_vacio()
        movimientos = [
            (0, 1), # Moviemiento hacia Derecha
            (1, 0), # Moviemiento hacia Abajo
            (0, -1),# Moviemiento hacia Izquierda
            (-1, 0) # Moviemiento hacia Arriba
        ]

        sucesores = []

        for di, dj in movimientos:
            ni = i + di
            nj = j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                nuevo_tablero = [fila.copy() for fila in self.tablero]
                nuevo_tablero[i][j], nuevo_tablero[ni][nj] = nuevo_tablero[ni][nj], nuevo_tablero[i][j]
                tablero_str = str(nuevo_tablero)
                if tablero_str not in visitados:
                    visitados.add(tablero_str)
                    sucesores.append(Nodo(nuevo_tablero, self, (ni, nj)))

        return sucesores

    # Metodo para obtener los sucesores validos del tablero
    def sucesores(self):
        i, j = self.obtener_vacio()
        movimientos = [
            (0, 1), # Moviemiento hacia Derecha
            (1, 0), # Moviemiento hacia Abajo
            (0, -1),# Moviemiento hacia Izquierda
            (-1, 0)]# Moviemiento hacia Arriba

        # Generamos los sucesores
        sucesores = []

        for di, dj in movimientos:
            # Validamos que el movimiento este dentro del tablero
            ni = i+di
            nj = j+dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                # Si el movimiento es valido, generamos un nuevo tablero y lo agregamos a la lista de los sucesores
                nuevo_tablero = [fila.copy() for fila in self.tablero]
                nuevo_tablero[i][j], nuevo_tablero[ni][nj] = nuevo_tablero[ni][nj], nuevo_tablero[i][j]
                sucesores.append(Nodo(nuevo_tablero, self, (ni, nj)))

        return sucesores

def DFS(inicio, objetivo):
    pila = deque([Nodo(inicio)])
    while pila:
        nodo = pila.pop()  # Pop obtiene y remueve el último elemento, que es el comportamiento de una pila.
        if nodo.tablero == objetivo:
            return nodo

        sucesores = nodo.obtener_sucesores()  # Cambiamos el método para que devuelva todos los sucesores.
        for sucesor in sucesores:
            pila.append(sucesor)

    return None

def es_soluble(tablero):
    aplanado = [num for fila in tablero for num in fila if num != "_"]
    inversiones = 0

    for i in range(len(aplanado)):
        for j in range(i + 1, len(aplanado)):
            if aplanado[i] > aplanado[j]:
                inversiones += 1

    return inversiones % 2 == 0

def desordenar_tablero(tablero):
    aplanado = [num for fila in tablero for num in fila]
    random.shuffle(aplanado)
    nuevo_tablero = [aplanado[i:i+3] for i in range(0, 9, 3)]

    intentos = 0
    while not es_soluble(nuevo_tablero):
        intentos += 1
        print(f"Intento {intentos}: El tablero no es soluble, creando uno nuevo...")
        random.shuffle(aplanado)
        nuevo_tablero = [aplanado[i:i+3] for i in range(0, 9, 3)]

    return nuevo_tablero
tablero_inicial = [[1, 2, 3],
                  [5, 6, "_"],
                  [7, 8, 4]]
tablero_objetivo = desordenar_tablero(tablero_inicial)
print("Tablero objetivo: ",tablero_objetivo)
# Empezamos el cronometro
start_time = time.time()
# Ejecutamos el algoritmo BFS
resultado = DFS(tablero_inicial, tablero_objetivo)
# Si encontramos el camino lo imprimimos
if resultado:
    # Terminamos el cronometro
    elapsed_time = time.time() - start_time
    print("¡Solución encontrada!")
    camino = []
    while resultado: # Recorremos el camino desde el nodo objetivo hasta el nodo inicial
        camino.append(resultado.tablero)
        resultado = resultado.padre
    print("Tiempo de ejecución: %.10f segundos." % elapsed_time)
    print("Número de movimientos: ", len(camino)-1)
else:
     # Terminamos el cronometro
    elapsed_time = time.time() - start_time
    print("Tiempo de ejecución: %.10f segundos." % elapsed_time)
    print("No se encontró solución.")
