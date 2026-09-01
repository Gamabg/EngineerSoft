import java.util.Scanner;

public class ArithmeticException {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número: ");
        int numero = scanner.nextInt();

        try {
            int resultado = 10 / numero;
            System.out.println("Resultado: " + resultado);
        } catch (java.lang.ArithmeticException e) {
            System.out.println("Erro: divisão por zero!");
        } finally {
            scanner.close();
        }
    }
}
