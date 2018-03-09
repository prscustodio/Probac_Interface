#include "Wire.h"

void setup() 
{
  // put your setup code here, to run once:
Serial.begin(9600);
Wire.begin();
pinMode(13,OUTPUT);
}

void loop() 
{
  
  // put your main code here, to run repeatedly:
if(Serial.available())
{
  int adress=0x01;
  char dado = Serial.read();
  int cont=0;
  byte init=0x50;
  byte operacao=0x48;
  byte sensor=0x01;
  byte finalizador=0x21;


  
 // Serial.println(dado);
  
  if (dado == ('f'))
  {
    for (cont;cont<2;cont=cont+1)
    {
    digitalWrite(13,HIGH);
    delay(500);
    digitalWrite(13,LOW);
    delay(500);
    Wire.beginTransmission(adress);
    int chkParcial=init^operacao;
    int chk= chkParcial^sensor;
    byte dadosi2c[5];
    dadosi2c[0]= init;
    dadosi2c[1]=operacao;
    dadosi2c[2]=sensor;
    dadosi2c[3]=chk;
    dadosi2c[4]=finalizador;
    //Wire.write(dadosi2c,5);
    Serial.print(Wire.read());
    Wire.endTransmission();
    
    }
    cont=0;
    //Serial.write(" ");
    Serial.write("ra");
    
  }
  if (dado == ('c'))
  {
    for (cont;cont<2;cont=cont+1)
    {
    digitalWrite(13,HIGH);
    delay(500);
    digitalWrite(13,LOW);
    delay(500);
    }
    cont=0;
    Serial.write("rb");
  }
  if (dado == ('v'))
  {
    for (cont;cont<3;cont=cont+1)
    {
    digitalWrite(13,HIGH);
    delay(500);
    digitalWrite(13,LOW);
    delay(500);
    }
    cont=0;
    Serial.write("rc");
  }
  
   
}
}
