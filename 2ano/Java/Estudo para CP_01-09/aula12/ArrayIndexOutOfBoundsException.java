public class ArrayIndexOutOfBoundsException {
    public static void main(String[] args) {
        try {
            int[] numeros = {1, 2, 3};
            System.out.println(numeros[10]);
        } catch (java.lang.ArrayIndexOutOfBoundsException e) {
            System.out.println("Erro: índice fora do intervalo.");
        } finally {
            System.out.println("Este bloco finally sempre executa.");
        }
    }
}
