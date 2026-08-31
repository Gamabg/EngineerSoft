public class ToCharArray {
    public static void main(String[] args) {
        String texto = "Java";
        char[] letras = texto.toCharArray();

        for (char letra : letras) {
            System.out.print(letra + " ");
        }
        System.out.println();
    }
}
