#include <dht.h>

int DHT11 = A1;
dht DHT; // Variável do tipo DHT
int BUZZER = 3;
int MQ02 = A0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600);
  
  pinMode (BUZZER, OUTPUT);
  pinMode (MQ02, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int MQ02_leitura = analogRead(MQ02);
  // Pega o nível de gás do sensor
  if ( MQ02_leitura > 500) {
    tone(BUZZER, 100);
  }
  Serial.print ("Gas = ");
  Serial.print(MQ02_leitura);
  
  // Parte do sensor de umidade e temperatura
  DHT.read11(DHT11);
  Serial.print (" Umidade = ");
  Serial.print ( DHT.humidity ); // DHT.humidity pega a umidade do sensor
  Serial.print (" %");
  
  Serial.print (" Temperatura = ");
  Serial.print ( DHT.temperature );
  Serial.println (" Celsius"); //DHT.temperature pega a temperatura do sensor
  
  delay (5000); 
}
