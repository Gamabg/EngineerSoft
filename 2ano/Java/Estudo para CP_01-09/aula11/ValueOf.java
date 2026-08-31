public class ValueOf {
    public static void main(String[] args) {
        int idade = 20;
        double preco = 49.99;

        String idadeTexto = String.valueOf(idade);
        String precoTexto = String.valueOf(preco);

        System.out.println("idade = " + idadeTexto);
        System.out.println("preco = " + precoTexto);
    }
}
