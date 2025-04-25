// Definindo os pinos
const int ledVerde = 7;   // LED verde no pino 7
const int ledVermelho = 5; // LED vermelho no pino 5
const int botao = 2;       // Botão no pino 2
 
int estadoBotao = 0;       // Estado do botão
bool pedestreAguardando = false; // Se o pedestre pressionou o botão
 
void setup() {
  // Configura os pinos dos LEDs como saída
  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  // Configura o pino do botão como entrada
  pinMode(botao, INPUT);
  // Inicializa o sistema com o LED vermelho aceso
  digitalWrite(ledVermelho, HIGH);
  digitalWrite(ledVerde, LOW);
}
 
void loop() {
  // Lê o estado do botão
  estadoBotao = digitalRead(botao);
  // Se o botão foi pressionado
  if (estadoBotao == HIGH && !pedestreAguardando) {
    pedestreAguardando = true;
    // Simula a mudança para o LED verde (indica que o pedestre pode atravessar)
    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledVermelho, LOW);
    // Espera por 5 segundos para o pedestre atravessar
    delay(5000);
    // Após 5 segundos, o farol volta a ficar vermelho
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, HIGH);
    // O pedestre não está mais aguardando
    pedestreAguardando = false;
  }
  // Aqui você pode colocar outros comportamentos ou tempos para os sinais
  // Exemplo, caso queira um tempo fixo para o semáforo funcionar de maneira independente.
}