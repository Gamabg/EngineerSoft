#define GREEN_LED_CAR 8 // LED verde carro
#define YELLOW_LED_CAR 9 // LED amarelo carro
#define RED_LED_CAR 10 // LED vermelho carro
 
#define GREEN_LED_PEDESTRIAN 11 // LED verde pedestre
#define RED_LED_PEDESTRIAN 12 // LED vermelho pedestre
 
void setup() {
  // Configura os pinos dos LEDs como saída
  pinMode(GREEN_LED_CAR, OUTPUT);
  pinMode(YELLOW_LED_CAR, OUTPUT);
  pinMode(RED_LED_CAR, OUTPUT);
  pinMode(GREEN_LED_PEDESTRIAN, OUTPUT);
  pinMode(RED_LED_PEDESTRIAN, OUTPUT);
}
 
void loop() {
  // Semáforo de carros (verde) e pedestre (vermelho)
  digitalWrite(GREEN_LED_CAR, HIGH);
  digitalWrite(YELLOW_LED_CAR, LOW);
  digitalWrite(RED_LED_CAR, LOW);
  digitalWrite(GREEN_LED_PEDESTRIAN, LOW);
  digitalWrite(RED_LED_PEDESTRIAN, HIGH);
  delay(1000); // Mantém por 1 segundo
  // Semáforo de carros (amarelo) e pedestre (vermelho)
  digitalWrite(GREEN_LED_CAR, LOW);
  digitalWrite(YELLOW_LED_CAR, HIGH);
  digitalWrite(RED_LED_CAR, LOW);
  digitalWrite(GREEN_LED_PEDESTRIAN, LOW);
  digitalWrite(RED_LED_PEDESTRIAN, HIGH);
  delay(1000); // Mantém por 1 segundo
  // Semáforo de carros (vermelho) e pedestre (verde)
  digitalWrite(GREEN_LED_CAR, LOW);
  digitalWrite(YELLOW_LED_CAR, LOW);
  digitalWrite(RED_LED_CAR, HIGH);
  digitalWrite(GREEN_LED_PEDESTRIAN, HIGH);
  digitalWrite(RED_LED_PEDESTRIAN, LOW);
  delay(1000); // Mantém por 1 segundo
}