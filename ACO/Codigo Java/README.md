# Ejemplos de uso

Tendremos que ir a la ubicacion del archivo. Para ejecutarlo hay que escribir una serie de comandos:
- javac principal.java
- java principal
## Observacion
El programa pedira la cantidad de iteraciones, hormigas y evaporacion. Para la evaporacion tendremos que ingresar un valor entre el 1 y el 0.

# Como funciona

## Hay 3 clases:
	1) hormiga: Esta clase, será la clase hormiga, que evaluara que ciudad visitar según la cantidad de feromonas que hayan.
	2) aco: donde se ejecutaran las iteraciones, aquí actuara la evaporación de feromonas, disminuirán en cada iteración.
	3) ciudad: Será un objeto en donde estará el id y las coordenadas de la ciudad.
	4) lectura: Donde se leerá el archivo.


## Como funcionara cada clase:

	1) hormiga: Contendrá un List con las ciudades visitadas, tendrá una función en donde según la cantidad de feromonas evaluara la probabilidad de ir a las ciudades, se escogerá de manera random, aunque las ciudades con las feromonas tenderán a tener un porcentaje mas alto de ser visitados primero. Cuando la hormiga termine su recorrido, este dejara una cierta cantidad de feromonas dependiendo de la calidad de su solución.
    2) aco: Este contendrá una matriz de feromonas, indicando la cantidad de feromonas de cada camino, este tendrá un tamaño de 100x100(en el caso del archivo), también, en cada iteración se evaporara el porcentaje que se haya ingresado en cada iteración. La matriz feromonas será una variable global, para que cada hormiga pueda modificarla cuando haya terminado su recorrido.
    3) ciudad: La ciudad solo contendrá las coordenadas y una función que servirá para calcular la distancia entre esa ciudad y la que se esta evaluando.
    4) lectura: Esta clase NO puede leer el encabezado del texto original, por lo que lo elimine, es mas fácil dejar el contenido que sirve para no hacer el código mas complejo.
