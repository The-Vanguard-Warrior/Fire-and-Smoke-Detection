int flame_sensor_pin = 4;       // initializing pin 4 as the sensor output pin
int flame_pin = HIGH;           // state of sensor

// PIN OF SIGNAL
#define THERMISTORPIN A0        
// resistance of termistor at 25 degrees C
#define THERMISTORNOMINAL 10000      
#define TEMPERATURENOMINAL 25   
// Accuracy - Higher number is bigger
#define NUMSAMPLES 10
// Beta coefficient from datasheet
#define BCOEFFICIENT 3950
// the value of the R1 resistor
#define SERIESRESISTOR 10000    
//prepare pole 
uint16_t samples[NUMSAMPLES];
 
void setup(void) {
  pinMode(flame_sensor_pin, INPUT);
  Serial.begin(9600);
}
 
void loop(void) {

  flame_pin = digitalRead(flame_sensor_pin);          // reading from the sensor
  uint8_t i;
  float average;
 
 // saving values from input to pole
  for (i=0; i< NUMSAMPLES; i++) {
   samples[i] = analogRead(THERMISTORPIN);
   delay(10);
  }
 
   // average value of input
  average = 0;
  for (i=0; i< NUMSAMPLES; i++) {
     average += samples[i];
  }
  average /= NUMSAMPLES;
 
  //resistance
  average = 1023 / average - 1;
  average = SERIESRESISTOR / average;

 //resistence to temperature
  float temperature;
  temperature = average / THERMISTORNOMINAL; 
  temperature = log(temperature);   
  temperature /= BCOEFFICIENT;                  
  temperature += 1.0 / (TEMPERATURENOMINAL + 273.15); 
  temperature = 1.0 / temperature;                 
  temperature -= 273.15;                         // convert to C


   if (flame_pin == LOW)                               // applying condition
  {
  Serial.println("FLAME, FLAME, FLAME");
  Serial.print("Temperature: "); 
  Serial.print(temperature);
  Serial.println("°C");
  }

 
  delay(1000);
}
