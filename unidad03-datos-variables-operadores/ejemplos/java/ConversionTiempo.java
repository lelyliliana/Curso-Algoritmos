public class ConversionTiempo {
    public static void main(String[] args) {
        int totalSegundos = 145;
        int minutos = totalSegundos / 60;
        int segundos = totalSegundos % 60;
        System.out.println(minutos + " minutos, " + segundos + " segundos");
    }
}
