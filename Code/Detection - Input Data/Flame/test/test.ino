int flame_sensor_pin = 4;       // initializing pin 4 as the sensor output pin

int flame_pin = HIGH;           // state of sensor
 
 
void setup()
{
  pinMode(flame_sensor_pin, INPUT);
  Serial.begin(9600);
}
 
 
void loop()
{
  flame_pin = digitalRead(flame_sensor_pin);          // reading from the sensor
  if (flame_pin == LOW)                               // applying condition
  {
    Serial.println("FLAME, FLAME, FLAME");
  }
}
 
