#include <dht.h>
dht DHT;

bool c = false;
unsigned long tprev = millis();
unsigned long tnow = millis();
#define R 3
#define G 5
#define B 6
#define Hum 7
#define Buzz 13

void setup() {
  Serial.begin(9600);
  pinMode(Buzz,OUTPUT);
  pinMode(R,OUTPUT);
  pinMode(G,OUTPUT);
  pinMode(B,OUTPUT);
  digitalWrite(Buzz , LOW);
}

void loop() {
  
  if(Serial.available() > 0){
    String in = Serial.readString();
    in.trim();
    
    if  (in.startsWith("$") && in.endsWith("$")){
      String buzz = in.substring(1,4);
      String red = in.substring(4,7);
      String green = in.substring(7,10);
      String blue = in.substring(10,13);
      
      if(buzz=="111"){
         digitalWrite(Buzz , HIGH);
      }else{
        digitalWrite(Buzz , LOW);
      }

      analogWrite(R ,red.toInt() );
      analogWrite(G ,green.toInt() );
      analogWrite(B ,blue.toInt() );
    }
  }else{
    tnow = millis();
    if(tnow-tprev >= 2000){
      int chk = DHT.read11(7);
      Serial.println(String(DHT.temperature)+" "+String(DHT.humidity));
      tprev= millis();
    }
  
  }

}
