public class IOException {
    public static void lerArquivo() throws java.io.IOException {
        throw new java.io.IOException("Arquivo não encontrado.");
    }

    public static void main(String[] args) {
        try {
            lerArquivo();
        } catch (java.io.IOException e) {
            System.out.println("Erro de entrada/saída: " + e.getMessage());
        }
    }
}
