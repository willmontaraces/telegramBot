#include <SoftwareSerial.h>
int pinWOL = 3;
int status = LOW;

SoftwareSerial BT1(2, 4); // RX | TX
void setup()
   { 
     Serial.begin(9600);
     Serial.println("Levantando el módulo HC-05");
     Serial.println("Esperando comandos AT:");
     BT1.begin(9600); 
     pinMode(pinWOL, OUTPUT);
     digitalWrite(pinWOL, LOW);
   }

void loop(){  
  if (BT1.available()){
    char rxChar = BT1.read();     
    Serial.println(rxChar);
    if(rxChar == 'W'){
      Serial.println("     WOL");
      BT1.write("O");
      BT1.flush();
      digitalWrite(pinWOL, HIGH);
      delay(500);
      digitalWrite(pinWOL, LOW);
      status = LOW;
    }else if(rxChar == 'I'){
      if(status == LOW)
        status = HIGH;
      else 
        status = LOW;
      digitalWrite(pinWOL, status);
      BT1.write(status);
      BT1.flush();
    }
    else{
      Serial.println("     NOT VALID");
      BT1.write("E");
      BT1.flush();
    }

  }       
}
