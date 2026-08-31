public class ExemploMetodosString {
    public static void main(String[] args) {
        String texto = "Java e Programacao";
        String nome = "Maria Silva";
        String nomeComEspacos = "   Java   ";
        String nome2 = "maria silva";
        String frase = "Joao;Maria;Ana";
        String vazio = "";

        System.out.println("--- charAt() ---");
        System.out.println(texto.charAt(0));

        System.out.println("--- codePointAt() ---");
        System.out.println(texto.codePointAt(0));

        System.out.println("--- compareTo() ---");
        System.out.println("banana".compareTo("caju"));

        System.out.println("--- compareToIgnoreCase() ---");
        System.out.println("JAVA".compareToIgnoreCase("java"));

        System.out.println("--- startsWith() ---");
        System.out.println(texto.startsWith("Java"));

        System.out.println("--- endsWith() ---");
        System.out.println(texto.endsWith("cao"));

        System.out.println("--- toCharArray() ---");
        char[] letras = texto.toCharArray();
        for (char letra : letras) {
            System.out.print(letra + " ");
        }
        System.out.println();

        System.out.println("--- getBytes() ---");
        byte[] bytes = texto.getBytes();
        System.out.println(bytes.length);

        System.out.println("--- isEmpty() ---");
        System.out.println(vazio.isEmpty());

        System.out.println("--- split() ---");
        String[] partes = frase.split(";");
        for (String parte : partes) {
            System.out.println(parte);
        }

        System.out.println("--- substring() ---");
        System.out.println(texto.substring(0, 4));

        System.out.println("--- toLowerCase() ---");
        System.out.println(nome.toLowerCase());

        System.out.println("--- toUpperCase() ---");
        System.out.println(nome.toUpperCase());

        System.out.println("--- trim() ---");
        System.out.println(nomeComEspacos.trim());

        System.out.println("--- valueOf() ---");
        int idade = 20;
        String idadeTexto = String.valueOf(idade);
        System.out.println(idadeTexto);

        System.out.println("--- format() ---");
        String formatado = String.format("Nome: %s - Idade: %d", nome, idade);
        System.out.println(formatado);
    }
}
