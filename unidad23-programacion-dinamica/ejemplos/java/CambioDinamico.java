import java.util.*;
public class CambioDinamico {
  static List<Integer> cambio(int[] originales, int total) {
    if (total < 0 || total > 10000 || originales.length == 0)
      throw new IllegalArgumentException("Dominio invalido");
    for (int m : originales)
      if (m <= 0)
        throw new IllegalArgumentException("Moneda positiva");
    int[] monedas = Arrays.stream(originales).distinct().sorted().toArray();
    int[] dp = new int[total + 1], previo = new int[total + 1];
    Arrays.fill(dp, total + 1);
    dp[0] = 0;
    for (int s = 1; s <= total; s++)
      for (int m : monedas)
        if (m <= s && dp[s - m] + 1 < dp[s]) {
          dp[s] = dp[s - m] + 1;
          previo[s] = m;
        }
    if (dp[total] == total + 1)
      return null;
    List<Integer> salida = new ArrayList<>();
    while (total > 0) {
      int m = previo[total];
      salida.add(m);
      total -= m;
    }
    return salida;
  }
  public static void main(String[] args) {
    System.out.println(cambio(new int[] {1, 3, 4}, 6));
  }
}
