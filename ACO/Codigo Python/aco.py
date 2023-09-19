import math
import random

# Clase para representar una ciudad
class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    def distancia(self, city):
        return math.sqrt((self.x - city.x)**2 + (self.y - city.y)**2)
class Ant:
    def __init__(self, ciudad_inicio):
        self.ciudad_inicio = [ciudad_inicio]
        self.ciudad_actual = ciudad_inicio
        self.visitados = [ciudad_inicio]

    def escoger_ciudad(self, feromonas, ciudades, alpha=1, beta=1):
        ciudades_disponibles = [city for city in ciudades if city not in self.visitados]
        if not ciudades_disponibles:
            return None

        # Logica de eleccion basada en feromonas y visibilidad o como algunos llaman conveniencia
        probabilidades = []
        for city in ciudades_disponibles:
            t = feromonas[self.ciudad_actual.id][city.id]  # feromona entre ciudad acutal y la ciudad que se esta evaluando
            n = 1 / self.ciudad_actual.distancia(city)  # visibilidad
            probabilidades.append(t**alpha * n**beta) # probabilidad de ir a la ciudad

        # Normalizar las probabilidades
        sum_prob = sum(probabilidades) # sumar todas las probabilidades
        probabilidades = [p/sum_prob for p in probabilidades] # dividir cada probabilidad entre la suma de todas las probabilidades

        # Elegir ciudad basado en probabilidad
        elegir = random.choices(ciudades_disponibles, probabilidades)[0]
        self.visitados.append(elegir)
        self.ciudad_actual = elegir
        return elegir
    def distancia_total(self):
        distancia = 0
        for i in range(len(self.visitados) - 1):
            distancia += self.visitados[i].distancia(self.visitados[i+1])
        return distancia
class ACO:
    def __init__(self, ciudades, num_hormigas=None):
        self.ciudades = ciudades
        self.feromonas = [[1 for _ in ciudades] for _ in ciudades]
        if num_hormigas is None:
            num_hormigas = len(ciudades)
        self.hormigas = [Ant(random.choice(ciudades)) for _ in range(num_hormigas)]

    def run(self, iteraciones=10, evaporacion=0.1, alpha=1, beta=1):
        todos_los_caminos = [] 
        for _ in range(iteraciones):
            for ant in self.hormigas:
                for _ in range(len(self.ciudades)-1):
                    ant.escoger_ciudad(self.feromonas, self.ciudades, alpha, beta)

            # Guardar los caminos y distancias de las hormigas en esta iteración
            for ant in self.hormigas:
                camino = [city.id for city in ant.visitados]
                distancia = ant.distancia_total()
                todos_los_caminos.append((camino, distancia))

            # Actualizar feromonas
            for i in range(len(self.feromonas)):
                for j in range(len(self.feromonas)):
                    self.feromonas[i][j] *= (1.0 - evaporacion)

            # Resetear hormigas
            for ant in self.hormigas:
                ant.visitados = [ant.visitados[0]]
                ant.ciudad_actual = ant.visitados[0]

        return todos_los_caminos


def cargar_tsp(filename):
    cities = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if "NODE_COORD_SECTION" in line:
                continue
            elif "EOF" in line:
                break
            else:
                parts = line.strip().split()
                id = int(parts[0]) - 1
                x = float(parts[1])
                y = float(parts[2])
                cities.append(City(id, x, y))
    return cities


archivo = "./ACO/a280.tsp"
cities = cargar_tsp(archivo)
aco = ACO(cities, num_hormigas=10)
resultados = aco.run()
for i, (camino, distancia) in enumerate(resultados, 1):
    print(f"Iteración {i} - Camino: {camino}, Distancia total: {distancia:.2f}")