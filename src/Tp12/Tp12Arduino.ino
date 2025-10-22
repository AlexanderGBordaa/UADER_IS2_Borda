//*----------------------------------------------------------
//* UADER - FCyT
//* Ingeniería de Software II
//* Dr. Pedro E. Colla
//*
//* TP12 - Taller sobre placa embebida
//*----------------------------------------------------------

const int pinButton = 2;
const int pinPot = A0;
const int ledOnboard = LED_BUILTIN;
const float VREF = 5.0;

void setup() {
  pinMode(ledOnboard, OUTPUT);
  pinMode(pinButton, INPUT);
  pinMode(pinPot, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(pinButton) == HIGH) {
    int rawValue = analogRead(pinPot);
    float voltage = rawValue * (VREF / 1023.0);

    Serial.print("Tension leida: ");
    Serial.print(voltage);
    Serial.println(" V");

    if (voltage <= VREF / 2) {
      digitalWrite(ledOnboard, HIGH);
    } else {
      digitalWrite(ledOnboard, LOW);
      delay(500);              // 0.5 s apagado
      digitalWrite(ledOnboard, HIGH);
      delay(500);              // 0.5 s encendido
    }
  }
}
