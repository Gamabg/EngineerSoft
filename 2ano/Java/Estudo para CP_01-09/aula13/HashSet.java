public class HashSet {
    public static void main(String[] args) {
        java.util.HashSet<String> alunos = new java.util.HashSet<>();

        alunos.add("João");
        alunos.add("Maria");
        alunos.add("João");
        alunos.add("Pedro");

        System.out.println("Conjunto de alunos: " + alunos);
        System.out.println("Tamanho: " + alunos.size());
    }
}
