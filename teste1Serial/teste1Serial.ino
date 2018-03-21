

#include <Wire.h>
//#include <String.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

#define adress  0x01
#define init  0x50
#define Start  0x05
#define Stop  0x03
#define Status  0x00
#define sensor1  0x04
#define sensor2  0x08
#define sensor3  0x10
#define sensor4  0x20
#define sensor5  0x40
#define Pause 'B' 
#define finalizador  0x21

char chk; 

char dadosi2c[10];
char dadoRecebido[10];

void sendPack(char bytes)
{
        char temp, i=0;
//        for (i;i<bytes-3;i++)
//        {
//          if (i!=4)temp^=dadosi2c[i];
//        }
//        dadosi2c[4]=0x50;
  
        //enviando solicitaçao via i2c
        lcd.clear();
        lcd.setCursor(0, 0);
        Wire.beginTransmission(adress);
        for (i=0;i<bytes;i++)
        {
            Wire.write(dadosi2c[i]);
            
            lcd.print(byte(dadosi2c[i]),HEX);
        }

        Wire.endTransmission();
  
}

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();
  pinMode(13, OUTPUT);
  lcd.begin (16, 2);
}

void loop()
{

  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    
    char dado = Serial.read();
    int  cont = 0;

    //declarando variaveis de comunicacao com filete

    //comando botao filete

    if (dado == ('f'))
    {
//      for (cont; cont < 2; cont = cont + 1)
//      {
        //escrevendo array de comunicaça
        dadosi2c[0] = init;
        dadosi2c[1] = adress;
        dadosi2c[2] = Start;
        dadosi2c[3] = sensor1;
        chk=dadosi2c[0]^dadosi2c[1]^dadosi2c[2]^dadosi2c[3];
        dadosi2c[4] = chk;
        dadosi2c[5] = finalizador;

        sendPack(6);
        
        Wire.requestFrom(adress, 6);

        while (Wire.available())
        {
         
        lcd.setCursor(0, 1);
        for (char i=0;i<6;i++)
         {
          dadoRecebido[i] = Wire.read();
          lcd.print(dadoRecebido[i],HEX);          
         }
        }
      
      Serial.write("ra");
    }
    
    // comandos botao concentrado
    if (dado == ('c'))
    {
     //escrevendo array de comunicaça
        dadosi2c[0] = init;
        dadosi2c[1] = adress;
        dadosi2c[2] = Stop;
        dadosi2c[3] = sensor1;
        chk=dadosi2c[0]^dadosi2c[1]^dadosi2c[2]^dadosi2c[3];
        dadosi2c[4] = chk;
        dadosi2c[5] = finalizador;

        sendPack(6);
        
        Wire.requestFrom(adress, 6);

        while (Wire.available())
        {
        lcd.setCursor(0, 1);
        for (char i=0;i<6;i++)
         {
          dadoRecebido[i] = Wire.read();

          lcd.print(dadoRecebido[i],HEX);
         } 
        }
      Serial.write("rb");
    }

    //comando botao varredura
    if (dado == ('v'))
    { 
        //escrevendo array de comunicaça
        dadosi2c[0] = init;
        dadosi2c[1] = adress;
        dadosi2c[2] = Status;
        dadosi2c[3] = sensor1;
        chk=dadosi2c[0]^dadosi2c[1]^dadosi2c[2]^dadosi2c[3];
        dadosi2c[4] = chk;
        dadosi2c[5] = finalizador;

        sendPack(6);
        
        Wire.requestFrom(adress, 7);

        while (Wire.available())
        {
        lcd.setCursor(0, 1);
        for (char i=0;i<7;i++)
         {
          char c =Wire.read();
          dadoRecebido[i] = c;
          if(dadoRecebido[2] == 0)
          {
              lcd.clear();
              lcd.setCursor(0, 0);
              lcd.print("STATUS SENSOR: ");
              lcd.setCursor(0, 1);
              if(dadoRecebido[4] == 'N') lcd.println("Em uso");else
              if(dadoRecebido[4] == 'F') lcd.println("Desligado");
          }
          lcd.print(dadoRecebido[i]);
         } 
        }
      Serial.write("rc");
    }


  }
}
