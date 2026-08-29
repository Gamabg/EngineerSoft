const int buttonPin = 2;      // Pino do botão
const int carRedPin = 12;      // Pino da luz vermelha do carro
const int carGreenPin = -10;    // Pino da luz verde do carro
const int pedestrianRedPin = -9;  // Pino da luz vermelha do pedestre
const int pedestrianGreenPin = 8; // Pino da luz verde do pedestre
 
unsigned long lastChangeTime = 0; // Tempo da última troca de sinal
unsigned long changeInterval = 5000; // Intervalo para troca das luzes (5 segundos)
bool isCarGreen = true; // Estado do semáforo do carro (verdadeiro = verde, falso = vermelho)
 
void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(carRedPin, OUTPUT);
  pinMode(carGreenPin, OUTPUT);
  pinMode(pedestrianRedPin, OUTPUT);
  pinMode(pedestrianGreenPin, OUTPUT);
 
  // Inicializa o semáforo
  digitalWrite(carRedPin, HIGH);
  digitalWrite(carGreenPin, LOW);
  digitalWrite(pedestrianRedPin, LOW);
  digitalWrite(pedestrianGreenPin, HIGH);
}
 
void loop() {
  // Lê o estado do botão
  int buttonState = digitalRead(buttonPin);
 
  // Se o botão for pressionado (LOW devido ao INPUT_PULLUP)
  if (buttonState == LOW) {
    // Atualiza o tempo da última mudança de sinal
    lastChangeTime = millis();
    // Alterna o estado do semáforo do carro
    isCarGreen = !isCarGreen;
  }
 
  // Verifica se já passou o tempo do intervalo
  if (millis() - lastChangeTime >= changeInterval) {
    if (isCarGreen) {
      // Carro verde, pedestre vermelho
      digitalWrite(carRedPin, LOW);
      digitalWrite(carGreenPin, HIGH);
      digitalWrite(pedestrianRedPin, HIGH);
      digitalWrite(pedestrianGreenPin, LOW);
    } else {
      // Carro vermelho, pedestre verde
      digitalWrite(carRedPin, HIGH);
      digitalWrite(carGreenPin, LOW);
      digitalWrite(pedestrianRedPin, LOW);
      digitalWrite(pedestrianGreenPin, HIGH);
    }
  }
}