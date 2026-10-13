import java.util.*;
public class BacktrackingSuma {
  static List<List<Integer>> soluciones(int[] valores, int objetivo) {
    if (objetivo < 0 || objetivo > 10000 || valores.length > 20)
      throw new IllegalArgumentException("Dominio invalido");
    for (int v : valores)
      if (v <= 0 || v > 10000)
        throw new IllegalArgumentException("Valor positivo hasta 10000");
    List<List<Integer>> salida = new ArrayList<>();
    explorar(valores, objetivo, 0, 0, new ArrayList<>(), salida);
    return salida;
  }
  static void explorar(int[] valores, int objetivo, int i, int suma, List<Integer> elegidos,
      List<List<Integer>> salida) {
    if (suma == objetivo) {
      salida.add(new ArrayList<>(elegidos));
      return;
    }
    if (i == valores.length || suma > objetivo)
      return;
    elegidos.add(i);
    explorar(valores, objetivo, i + 1, suma + valores[i], elegidos, salida);
    elegidos.remove(elegidos.size() - 1);
    explorar(valores, objetivo, i + 1, suma, elegidos, salida);
  }
  public static void main(String[] args) {
    System.out.println(soluciones(new int[] {2, 3, 5}, 5));
  }
}
