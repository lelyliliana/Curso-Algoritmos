import java.util.Arrays;

public class Ordenamientos {
    static int[] burbuja(int[] datos) {
        int[] a = Arrays.copyOf(datos, datos.length);
        for (int limite = a.length - 1; limite > 0; limite--)
            for (int i = 0; i < limite; i++)
                if (a[i] > a[i + 1]) {
                    int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t;
                }
        return a;
    }

    static int[] seleccion(int[] datos) {
        int[] a = Arrays.copyOf(datos, datos.length);
        for (int i = 0; i < a.length - 1; i++) {
            int menor = i;
            for (int j = i + 1; j < a.length; j++)
                if (a[j] < a[menor]) menor = j;
            int t = a[i]; a[i] = a[menor]; a[menor] = t;
        }
        return a;
    }

    static int[] insercion(int[] datos) {
        int[] a = Arrays.copyOf(datos, datos.length);
        for (int i = 1; i < a.length; i++) {
            int actual = a[i], j = i - 1;
            while (j >= 0 && a[j] > actual) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = actual;
        }
        return a;
    }
    public static void main(String[] args) {
        int[] datos = {4, 1, 3, 1};
        System.out.println("Burbuja: " + Arrays.toString(burbuja(datos)));
        System.out.println("Seleccion: " + Arrays.toString(seleccion(datos)));
        System.out.println("Insercion: " + Arrays.toString(insercion(datos)));
        System.out.println("Entrada conservada: " + Arrays.toString(datos));
    }
}
