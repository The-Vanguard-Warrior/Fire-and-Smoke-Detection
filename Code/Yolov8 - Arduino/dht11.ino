#include <DHT.h>
#define DHTPIN 4
DHT dht(DHTPIN, DHT11);
void setup() {
  Serial.begin(9600);
  dht.begin();
}

char a;
void loop() {
  a  = Serial.read();
  if(a == 't'){
    float t = dht.readTemperature(); 
    Serial.println(t);
  } else if(a == 'h'){
    float h = dht.readHumidity();
    Serial.println(h);
  }
  a = 0 ;
  delay(10);
}