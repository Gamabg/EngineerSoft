#define GREEN_LED 8 // LED verde
#define YELLOW_LED 9 // LED amarelo
#define RED_LED 10 // LED vermelho
 
void setup() {
  // Configura os pinos dos LEDs como saida
  pinMode(GREEN_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
}
 
void loop() {
  // Estado OK: LED verde aceso, outros apagados
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(RED_LED, LOW);
  delay(1000); // Mantem o estado por 1 segundo
 
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(YELLOW_LED, HIGH);
  digitalWrite(RED_LED, LOW);
  delay(1000);
 
  digitalWrite(GREEN_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(RED_LED, HIGH);
  delay(1000);
}
 
let titulo = "Aprender Java"
 
let descrição = "Estudar manipulação de string"
 
console.log(titulo, typeof(titulo))
console.log(descrição, typeof(descrição))
 
console.log("Tamanho da variavel Titulo:", titulo.length)
console.log("Tamanho da variavel Descrição:", descrição.length)
 
console.log("Primeiro caractere do titulo:", titulo[0])
console.log("Primeiro caractere da descreição:", descrição[0])
 
console.log("Primeiro caractere do titulo:", titulo[titulo.length -1])
 
const palavra = "palavra"
 
console.log("Caractere na posição 3", palavra.charAt(3))
 
let categoria = "Estudo"
let infoCompleta = "Categoria: " + categoria + "-" + titulo
 
console.log(infoCompleta)
 
let incocompleta2 = `categoria: ${categoria} - ${titulo}`
console.log(incocompleta2)
 
let texto1 = "Posição de Javascript"
console.log(texto1.indexOf("Javascript"))
console.log(texto1.includes("Javascript"))
console.log(texto1.startsWith("Posição"))
console.log(texto1.startsWith("Javascript"))
