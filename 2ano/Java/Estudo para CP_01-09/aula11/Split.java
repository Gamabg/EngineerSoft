public class Split {
    public static void main(String[] args) {
        String frase = "Joao;Maria;Ana";
        String[] partes = frase.split(";");

        for (String parte : partes) {
            System.out.println(parte);
        }
    }
}
