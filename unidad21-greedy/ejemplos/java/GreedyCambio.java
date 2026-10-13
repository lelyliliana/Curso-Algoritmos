import java.util.*;
public class GreedyCambio {
  static List<Integer> cambio(int[] monedas, int total) {
    if (total < 0 || total > 10000 || monedas.length == 0)
      throw new IllegalArgumentException("Dominio invalido");
    TreeSet<Integer> valores = new TreeSet<>(Comparator.reverseOrder());
    for (int m : monedas) {
      if (m <= 0)
        throw new IllegalArgumentException("Moneda positiva");
      valores.add(m);
    }
    List<Integer> resultado = new ArrayList<>();
    for (int m : valores) {
      int cantidad = total / m;
      for (int i = 0; i < cantidad; i++) resultado.add(m);
      total %= m;
    }
    return total == 0 ? resultado : null;
  }
  public static void main(String[] args) {
    System.out.println(cambio(new int[] {1, 3, 4}, 6));
  }
}
