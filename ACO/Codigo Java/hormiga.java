import java.util.ArrayList;
import java.util.List;

public class hormiga {
    int id, iteracion, recorrido;
    List<ciudad> ciudades; // Lista de ciudades
    List<ciudad> camino = new ArrayList<ciudad>(); // Camino que va recorriendo la hormiga
    List<ciudad> visitados = new ArrayList<ciudad>(); // Lista de ciudades visitadas
    List<ciudad> novisitados = new ArrayList<ciudad>();// Lista de ciudades no visitadas

    public void run() {
        // Empezamos a recorrer segun este punto
        int i = 0;
        while (visitados.size() < ciudades.size()) {
            ciudad ciudad_elegida = seleccionarSiguienteCiudad();
            if (ciudad_elegida == null) {
                System.out.println("ERROR");
            } else {
                visitados.add(ciudad_elegida); // La añadimos a la lista de visitados
                camino.add(ciudad_elegida); // La añadimos al camino
                buscarEliminar(ciudad_elegida); // Eliminamos la ciudad de la lista de ciudades
                recorrido += ciudad_elegida.calcularDistancia(visitados.get(i)); // Calculamos la distancia entre la ciudad actual y la siguiente
                i++;
            }
        }
        System.out.println("Hormiga " + id + " de la iteracion " + iteracion+" ha recorrido: "+recorrido);
        depositarFeromonas();
    }

    public void depositarFeromonas() {
        double deposito = 1.0 / recorrido;
        for (int i = 0; i < camino.size() - 1; i++) {
            int ciudadActual = camino.get(i).getId() - 1;
            int ciudadSiguiente = camino.get(i + 1).getId() - 1;
            aco.feromonas[ciudadActual][ciudadSiguiente] += deposito;
            aco.feromonas[ciudadSiguiente][ciudadActual] += deposito;
        }
    }

    public ciudad seleccionarSiguienteCiudad() {
        double[] probabilidadTransicion = new double[novisitados.size()];
        double sum = 0.0;

        // Calcule las probabilidades de transición
        for (int i = 0; i < novisitados.size(); i++) {
            if (novisitados.get(i) == null) { // Si la ciudad ya fue visitada, la probabilidad es 0
                probabilidadTransicion[i] = 0;
                continue;
            }
            ciudad ciudad = novisitados.get(i);
            ciudad ciudadActual = visitados.get(visitados.size() - 1);

            int indexActual = ciudadActual.getId() - 1;
            int indexCiudad = ciudad.getId() - 1;

            if (indexActual == indexCiudad) { // Si la ciudad actual es la misma que la ciudad a evaluar, la
                                              // probabilidad es 0
                probabilidadTransicion[i] = 0;
                continue;
            }

            double feromona = aco.feromonas[indexActual][indexCiudad];
            double visibilidad = 1.0 / ciudad.calcularDistancia(ciudadActual);
            

            probabilidadTransicion[i] = feromona * visibilidad;

            sum += probabilidadTransicion[i];
        }

        // Normalizar las probabilidades
        for (int i = 0; i < probabilidadTransicion.length; i++) {
            probabilidadTransicion[i] /= sum;
        }

        // Genera un número aleatorio entre 0 y la suma total
        double rand = Math.random() * sum;
        double acumulado = 0.0;
        for (int i = 0; i < novisitados.size(); i++) {
            if (novisitados.get(i) == null) {
                continue;
            }
            acumulado += probabilidadTransicion[i];
            if (rand <= acumulado) {
                return novisitados.get(i);
            }
        }
        return null;// En teoría nunca deberíamos llegar a este punto
    }

    public void setData(int id,int iteracion, List<ciudad> ciudades, ciudad ciudad_comienzo) {
        this.id = id;
        this.iteracion = iteracion;
        this.ciudades = ciudades;
        this.novisitados = new ArrayList<ciudad>(ciudades);
        this.visitados.add(ciudad_comienzo); // Añadimos la ciudad de comienzo a la lista de visitados
        this.camino.add(ciudad_comienzo); // Añadimos la ciudad de comienzo al camino
        buscarEliminar(ciudad_comienzo); // Eliminamos las ciudades que se van visitando
    }

    public void buscarEliminar(ciudad ciudad_eliminar) {
        for (int i = 0; i < novisitados.size(); i++) {
            if (novisitados.get(i).getId() == ciudad_eliminar.getId()) {
                novisitados.remove(i);
                break;
            }
        }
    }
}
