public class ArrayList {
    public static void main(String[] args) {
        java.util.ArrayList<String> nomes = new java.util.ArrayList<>();

        nomes.add("Ana");
        nomes.add("Bruno");
        nomes.add("Carla");
        nomes.add("Bruno");

        System.out.println("Lista de nomes: " + nomes);
        System.out.println("Tamanho: " + nomes.size());
        System.out.println("Elemento na posição 1: " + nomes.get(1));
    }
}
