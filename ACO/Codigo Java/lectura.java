import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class lectura {


     public List<ciudad> leer(String filename) throws IOException {
        List<ciudad> ciudades = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.trim().split("\\s+");
                if (parts.length != 3) {
                    continue; // Skip invalid lines
                }
                int index = Integer.parseInt(parts[0]);
                int x = Integer.parseInt(parts[1]);
                int y = Integer.parseInt(parts[2]);
                ciudades.add(new ciudad(index, x, y));
            }
        }
        return ciudades;
    }
}
