int luces[] = {3, 5, 6, 9, 10, 11};

void setup() {
  for(int i = 0; i <= 5; i++){
    pinMode(luces[i], OUTPUT);
  }
  randomSeed(analogRead(A0));
}

void loop() {
  int aleatorio = random(2);
  switch(aleatorio) {
    case 0:
      encendido_pwm();
      break;
    case 1:
      giro();
      break;
  }
}

void giro() {  
  for(int i = 0; i <= 5; i++){
    digitalWrite(luces[i], HIGH);
    delay(100);
  }
  for(int i = 0; i <= 5; i++){
    digitalWrite(luces[i], LOW);
    delay(100);
  }
}

void encendido_pwm() {
  for(int j = 0; j <= 255; j++) {
    for(int i = 0; i <= 5; i++) {
      analogWrite(luces[i], j);
    }
    delay(5);
  }

  for(int j = 0; j <= 255; j++) {
    for(int i = 0; i <= 5; i++) {
      analogWrite(luces[i], 255 - j);
    }
    delay(5);
  }
}

