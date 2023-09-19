import java.io.IOException;
import java.util.List;

public class principal {
    public static void main(String[] args) throws IOException {
        lectura leer_archivo = new lectura();
        List<ciudad> ciudades = leer_archivo.leer("./a280.tsp");
        aco aco = new aco();
        aco.setParametros(20, 10, 0.1, ciudades);
        aco.run();
    }
}