import java.util.List;

public class aco {
    int iteraciones,hormigas;
    double evaporacion;
    List<ciudad> ciudades;
    static double feromonas[][];

    public void run(){
        ciudad ciudad_random = ciudad_random(); // Escogemos una ciudad al azar
        System.out.println("Ciudad random: " + ciudad_random.getId());
        for (int i = 0; i < iteraciones; i++) {
            for (int j = 0; j < hormigas; j++) {
                hormiga ant = new hormiga();
                ant.setData(j,i, this.ciudades, ciudad_random);
                ant.run();
            }
            evaporar();
        }
    }

    public void imprimirFeromonas(){
        for (int i = 0; i < ciudades.size(); i++) {
            for (int j = 0; j < ciudades.size(); j++) {
                System.out.print(feromonas[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void evaporar(){
        for (int i = 0; i < ciudades.size(); i++) {
            for (int j = 0; j < ciudades.size(); j++) {
                feromonas[i][j] *= (1 - evaporacion);
            }
        }
    }

    public void setParametros(int iteraciones, int hormigas, double evaporacion, List<ciudad> ciudades){
        this.iteraciones = iteraciones;
        this.hormigas = hormigas;
        this.evaporacion = evaporacion;
        this.ciudades = ciudades;
        feromonas = new double[ciudades.size()][ciudades.size()];
        inicializarFeromonas(ciudades.size());
    }

    public ciudad ciudad_random() {
        // Escogemos una ciudad al azar
        int random = (int) (Math.random() * ciudades.size());
        ciudad ciudad_random = ciudades.get(random);
        return ciudad_random;
    }

    public void inicializarFeromonas(int size){
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                feromonas[i][j] = 0.1;
            }
        }
    }

    public static void updateFeromonas(ciudad ciudad1, ciudad ciudad2, double valor){
        int idciudad1 = ciudad1.getId();
        int idciudad2 = ciudad2.getId();
        feromonas[idciudad1][idciudad2] = valor;
    }
}
