public class Busquedas {
    static int lineal(int[] datos, int objetivo) {
        for (int i = 0; i < datos.length; i++)
            if (datos[i] == objetivo) return i;
        return -1;
    }
    static int binaria(int[] datos, int objetivo) {
        int izquierda = 0, derecha = datos.length - 1;
        while (izquierda <= derecha) {
            int medio = (izquierda + derecha) / 2;
            if (datos[medio] == objetivo) return medio;
            if (datos[medio] < objetivo) izquierda = medio + 1;
            else derecha = medio - 1;
        }
        return -1;
    }
    public static void main(String[] args) {
        int[] datos = {2,5,8,12,16,23,38};
        System.out.println(lineal(datos, 16));
        System.out.println(binaria(datos, 16));
    }
}
