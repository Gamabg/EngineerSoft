package exc50;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        HashMap<Integer, Cliente> clientes = new HashMap<>();

        Scanner sc = new Scanner(System.in);

        int id = 0;
        String continuar;

        System.out.println("..:: Cadastro de Clientes ::..");
        while (true) {
            Cliente c = new Cliente();

            id++;
            c.setId(id);

            System.out.print("Digite o nome do cliente: ");
            c.setNome(sc.nextLine());

            System.out.print("Digite a idade do cliente: ");
            while (!sc.hasNextInt()) {
                System.out.print("Valor inválido. Digite a idade novamente: ");
                sc.next();
            }
            c.setIdade(sc.nextInt());
            sc.nextLine();

            System.out.print("Digite o e-mail do cliente: ");
            c.setEmail(sc.nextLine());

            clientes.put(id, c);

            System.out.print("Deseja realizar outro cadastro? (S/N): ");
            continuar = sc.nextLine().trim().toUpperCase();

            if (continuar.equals("N"))
                break;
        }

        clientes.forEach((chave, valor) -> {
            System.out.print("Cliente " + chave + "\n" + valor);
        });
    }
}
