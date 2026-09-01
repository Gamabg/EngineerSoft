public class HashMap {
    public static void main(String[] args) {
        java.util.HashMap<String, Integer> idades = new java.util.HashMap<>();

        idades.put("Ana", 20);
        idades.put("Bruno", 18);
        idades.put("Carla", 22);
        idades.put("Ana", 21);

        System.out.println("Mapa de idades: " + idades);
        System.out.println("Idade de Ana: " + idades.get("Ana"));
        System.out.println("Chaves: " + idades.keySet());
    }
}
