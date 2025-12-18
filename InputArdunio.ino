

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Ardunio Systems Active");
  pinMode(2,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);
  pinMode(7,INPUT_PULLUP);
  pinMode(8,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(2) == LOW) {
    Serial.println("CLICK");
    delay(100);
  }

  if (digitalRead(4) == LOW) {
    delay(600);
    Serial.println("MIDDLE");
    delay(100);
  }

    if (digitalRead(7) == LOW) {
    delay(600);
    Serial.println("RING");
    delay(100);
  }

  if (digitalRead(8) == LOW) {
    delay(750);
    Serial.println("OPEN_DC");
    delay(100);
  }
}
