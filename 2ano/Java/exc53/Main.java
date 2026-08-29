import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Cliente> clientes = new ArrayList<>();

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

            int idade;
            while (true) {
                System.out.print("Digite a idade do cliente: ");
                while (!sc.hasNextInt()) {
                    System.out.print("Valor inválido. Digite a idade novamente: ");
                    sc.next();
                }
                idade = sc.nextInt();
                sc.nextLine();

                if (idade < 0) {
                    System.out.println("A idade não pode ser negativa.");
                    continue;
                }
                break;
            }
            c.setIdade(idade);

            System.out.print("Digite o e-mail do cliente: ");
            c.setEmail(sc.nextLine());

            clientes.add(c);

            String resposta;
            while (true) {
                System.out.print("Deseja realizar outro cadastro? (S/N): ");
                resposta = sc.nextLine().trim().toUpperCase();

                if (resposta.equals("S") || resposta.equals("N")) {
                    break;
                }
                System.out.println("Resposta inválida! Digite apenas S ou N.");
            }
            continuar = resposta;

            if (continuar.equals("N"))
                break;
        }

        System.out.println("\n..:: Clientes Cadastrados ::..");
        for (Cliente valor : clientes) {
            System.out.println("Cliente " + valor.getId());
            System.out.println("Nome: " + valor.getNome());
            System.out.println("Idade: " + valor.getIdade());
            System.out.println("E-mail: " + valor.getEmail());
            System.out.println("--------------------------");
        }

        sc.close();
    }
}