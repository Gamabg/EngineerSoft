import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class main {

    public static void Main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, produto> produtos = new HashMap<>();

        boolean continuar = true;

        while (continuar) {
            System.out.println("\n===== Cadastro de Produto =====");

            System.out.print("ID do produto: ");
            int id = Integer.parseInt(sc.nextLine().trim());

            System.out.print("Nome do produto: ");
            String nome = sc.nextLine().trim();

            System.out.print("Preco do produto: ");
            double preco = Double.parseDouble(sc.nextLine().trim());

            System.out.print("Quantidade do produto: ");
            double quantidade = Double.parseDouble(sc.nextLine().trim());

            Categoria categoria = null;

            System.out.print("Este produto possui categoria? (s/n): ");
            String resposta = sc.nextLine().trim().toLowerCase();

            if (resposta.equals("s")) {
                System.out.print("ID da categoria: ");
                int catId = Integer.parseInt(sc.nextLine().trim());

                System.out.print("Nome da categoria: ");
                String catNome = sc.nextLine().trim();

                categoria = new Categoria(catId, catNome);
            }

            produto produto = new produto(id, nome, preco, quantidade, categoria);
            produtos.put(id, produto);

            System.out.print("\nDeseja cadastrar outro produto? (s/n): ");
            String outra = sc.nextLine().trim().toLowerCase();
            if (!outra.equals("s")) {
                continuar = false;
            }
        }

        System.out.println("\n===== Produtos Cadastrados =====");
        for (produto p : produtos.values()) {
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