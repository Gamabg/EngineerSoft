import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);

        ArrayList<Cliente> listaClientes = new ArrayList<Cliente>();

        int opcao = 0;
        int id;
        Cliente cli;
        int id_cliente = 0;
        String possuiConta;

        do {
            System.out.printf("===> Sistema de Cadastro de Clientes <===\n\n");
            System.out.printf("Escolha uma opção:\n");
            System.out.printf("1 - Incluir \n" +
                    "2 - Atualizar \n" +
                    "3 - Excluir \n" +
                    "4 - Exibir \n" +
                    "5 - Sair\n\n");

            System.out.printf("Digite a opção desejada: ");

            try {
                opcao = ler.nextInt();
                ler.nextLine(); // consome a quebra de linha pendente
            } catch (InputMismatchException e) {
                System.out.println("Opção inválida! Digite um número.");
                ler.nextLine(); // limpa o buffer
                opcao = 0;
                continue;
            }

            if (opcao == 1) {
                Cliente cliente = new Cliente();

                id_cliente++;
                cliente.setId(id_cliente);

                System.out.print("Digite o seu nome: ");
                cliente.setNome(ler.nextLine());

                try {
                    System.out.print("Digite a sua idade: ");
                    cliente.setIdade(Integer.parseInt(ler.nextLine()));
                } catch (NumberFormatException e) {
                    System.out.println("Idade inválida! Cadastro cancelado.");
                    id_cliente--;
                    continue;
                }

                System.out.print("Digite o seu e-mail: ");
                cliente.setEmail(ler.nextLine());

                System.out.print("Possui conta bancária? S/N: ");
                possuiConta = ler.nextLine().toUpperCase();

                if (possuiConta.equals("S")) {
                    ContaBancaria conta = new ContaBancaria();

                    System.out.print("Digite a agência: ");
                    conta.setAgencia(ler.nextLine());

                    System.out.print("Digite o número: ");
                    conta.setNumero(ler.nextLine());

                    conta.setSaldo(0);

                    cliente.setConta(conta);
                } else {
                    cliente.setConta(null);
                }

                listaClientes.add(cliente);

                System.out.println("Cliente incluído com sucesso!\n");
            } else if (opcao == 2) {
                for (Cliente valor : listaClientes) {
                    System.out.println("ID: " + valor.getId() + " - " + valor.exibirNomeIdade());
                }

                System.out.print("Digite o ID do cliente que você deseja atualizar: ");
                try {
                    id = Integer.parseInt(ler.nextLine());
                } catch (NumberFormatException e) {
                    System.out.println("ID inválido!\n");
                    continue;
                }

                cli = buscarPorId(listaClientes, id);

                if (cli != null) {
                    System.out.print("Digite o seu novo nome: ");
                    cli.setNome(ler.nextLine());

                    try {
                        System.out.print("Digite a sua nova idade: ");
                        cli.setIdade(Integer.parseInt(ler.nextLine()));
                    } catch (NumberFormatException e) {
                        System.out.println("Idade inválida! Atualização de idade ignorada.");
                    }

                    System.out.print("Digite o seu novo e-mail: ");
                    cli.setEmail(ler.nextLine());

                    System.out.println("Cliente atualizado com sucesso!\n");
                } else {
                    System.out.println("Cliente não encontrado!\n");
                }
            } else if (opcao == 3) {
                for (Cliente valor : listaClientes) {
                    System.out.println("ID: " + valor.getId() + " - " + valor.exibirNomeIdade());
                }

                System.out.print("Digite o ID do cliente que você deseja excluir: ");
                try {
                    id = Integer.parseInt(ler.nextLine());
                } catch (NumberFormatException e) {
                    System.out.println("ID inválido!\n");
                    continue;
                }

                cli = buscarPorId(listaClientes, id);

                if (cli != null) {
                    listaClientes.remove(cli);
                    System.out.println("Cliente excluído com sucesso!\n");
                } else {
                    System.out.println("Cliente não encontrado!\n");
                }
            } else if (opcao == 4) {
                for (Cliente valor : listaClientes) {
                    System.out.println("ID: " + valor.getId() + " - " + valor.exibirNomeIdade());

                    if (valor.getConta() != null)
                        System.out.println(valor.exibirDadosConta());
                }
                System.out.println();
            }

        } while ((opcao >= 1) && (opcao <= 4));

        ler.close();
    }

    private static Cliente buscarPorId(ArrayList<Cliente> lista, int id) {
        for (Cliente c : lista) {
            if (c.getId() == id) {
                return c;
            }
        }
        return null;
    }
}