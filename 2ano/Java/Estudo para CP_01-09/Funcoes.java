public class Funcoes {

    public static void main(String[] args) {
        String valor = "FIAP - Joseffe";

        System.out.println(valor.compareTo("FIAP - Joseffe") == 0 ? true : false);
        System.out.println(valor.compareTo("FIAP - JOSEFFE") == 0 ? true : false);
        System.out.println(valor.compareToIgnoreCase("FIAP - JOSEFFE") == 0 ? true : false);
    }
}
