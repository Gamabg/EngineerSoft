import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static String lerLinha(Scanner sc, String mensagem) {
        while (true) {
            System.out.print(mensagem);
            if (!sc.hasNextLine()) {
                System.out.println("\nEntrada encerrada. Finalizando...");
                System.exit(0);
            }

            String linha = sc.nextLine().trim();
            if (!linha.isEmpty()) {
                return linha;
            }

            System.out.println("Valor vazio. Tente novamente.");
        }
    }

    private static int lerInteiro(Scanner sc, String mensagem) {
        while (true) {
            String valor = lerLinha(sc, mensagem);
            try {
                return Integer.parseInt(valor);
            } catch (NumberFormatException e) {
                System.out.println("Digite um número inteiro válido.");
            }
        }
    }

    private static double lerDouble(Scanner sc, String mensagem) {
        while (true) {
            String valor = lerLinha(sc, mensagem);
            try {
                return Double.parseDouble(valor);
            } catch (NumberFormatException e) {
                System.out.println("Digite um número válido.");
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, Produto> produtos = new HashMap<>();

        boolean continuar = true;

        while (continuar) {
            System.out.println("\n===== Cadastro de Produto =====");

            int id = lerInteiro(sc, "ID do produto: ");
            String nome = lerLinha(sc, "Nome do produto: ");
            double preco = lerDouble(sc, "Preco do produto: ");
            double quantidade = lerDouble(sc, "Quantidade do produto: ");

            Categoria categoria = null;

            String resposta = lerLinha(sc, "Este produto possui categoria? (s/n): ").toLowerCase();
            if (resposta.equals("s")) {
                int catId = lerInteiro(sc, "ID da categoria: ");
                String catNome = lerLinha(sc, "Nome da categoria: ");
                categoria = new Categoria(catId, catNome);
            }

            Produto produto = new Produto(id, nome, preco, quantidade, categoria);
            produtos.put(id, produto);

            String outra = lerLinha(sc, "\nDeseja cadastrar outro produto? (s/n): ").toLowerCase();
            if (!outra.equals("s")) {
                continuar = false;
            }
        }

        System.out.println("\n===== Produtos Cadastrados =====");
        for (Produto p : produtos.values()) {
            System.out.println("--------------------------------");
            System.out.println(p.exibirNomePreco());
            System.out.println(p.exibirNomeQuantidade());

            if (p.getCategoria() != null) {
                System.out.println("Categoria: " + p.getCategoria().getNome()
                        + " (ID: " + p.getCategoria().getId() + ")");
            } else {
                System.out.println("Categoria: Nao informada");
            }
        }
        System.out.println("--------------------------------");

        sc.close();
    }
}