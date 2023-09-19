import java.lang.Math;
public class ciudad {
    int id;
    int x;
    int y;
    public ciudad(int id,int x, int y) {
        this.id = id;
        this.x = x;
        this.y = y;
    }
    public double calcularDistancia(ciudad ciudad) {
        double distancia = Math.sqrt(Math.pow((this.x-ciudad.getX()), 2) + Math.pow((this.y-ciudad.getY()), 2));
        if (distancia == 0) {
            System.out.println("QUEEEEEEEEEEEEEE, distancia 0, ciudad actual: " + this.id + " ciudad siguiente: " + ciudad.getId() + " x: " + this.x + " y: " + this.y + " x2: " + ciudad.getX() + " y2: " + ciudad.getY() + " distancia: " + distancia);
        }
        return distancia;
    }
    public int getId() {
        return this.id;
    }
    public int getX() {
        return this.x;
    }
    public int getY() {
        return this.y;
    }
}
