public class Format {
    public static void main(String[] args) {
        String nome = "Maria";
        int idade = 21;

        String texto = String.format("Nome: %s | Idade: %d", nome, idade);
        System.out.println(texto);
    }
}
