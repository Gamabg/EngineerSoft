public class CompareToIgnoreCase {
    public static void main(String[] args) {
        String a = "JAVA";
        String b = "java";

        System.out.println("JAVA.compareToIgnoreCase(java) => " + a.compareToIgnoreCase(b));
    }
}
