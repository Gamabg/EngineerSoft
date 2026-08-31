public class GetBytes {
    public static void main(String[] args) {
        String texto = "Java";
        byte[] bytes = texto.getBytes();

        System.out.println("Quantidade de bytes: " + bytes.length);
        for (byte b : bytes) {
            System.out.println(b);
        }
    }
}
