public class Exception {
    public static void main(String[] args) {
        try {
            int[] valores = {10, 20};
            System.out.println(valores[5]);
        } catch (java.lang.Exception e) {
            System.out.println("Exceção genérica capturada: " + e.getClass().getSimpleName());
        }
    }
}
