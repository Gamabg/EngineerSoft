public class IllegalArgumentException {
    public static void validarIdade(int idade) {
        if (idade < 18) {
            throw new java.lang.IllegalArgumentException("Idade inválida. É preciso ter 18 anos ou mais.");
        }
        System.out.println("Cadastro permitido.");
    }

    public static void main(String[] args) {
        try {
            validarIdade(15);
        } catch (java.lang.IllegalArgumentException e) {
            System.out.println("Erro capturado: " + e.getMessage());
        }
    }
}
