import java.io.IOException;
import java.util.List;

public class principal {
    public static void main(String[] args) throws IOException {

        // Pedimos la cantidad de iteraciones
        System.out.println("Ingrese la cantidad de iteraciones: ");
        int iteraciones = Integer.parseInt(System.console().readLine());
        // Pedimos la cantidad de hormigas
        System.out.println("Ingrese la cantidad de hormigas: ");
        int hormigas = Integer.parseInt(System.console().readLine());
        // Pedimos la evaporacion por iteracion
        System.out.println("Ingrese la evaporacion por iteracion: ");
        double evaporacion = Double.parseDouble(System.console().readLine());
        lectura leer_archivo = new lectura();
        List<ciudad> ciudades = leer_archivo.leer("./a280.tsp");
        aco aco = new aco();
        aco.setParametros(iteraciones, hormigas, evaporacion, ciudades);
        aco.run();
    }
}