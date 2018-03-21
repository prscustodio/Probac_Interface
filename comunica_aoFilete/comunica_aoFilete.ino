

#include <Wire.h>
//#include <String.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 2, 1, 0, 4, 5, 6, 7, 3, POSITIVE);

//variaveis
//#define               SERIAL_DEBUG
#define READ_GREEN    12
#define STATUS        0x00
#define Start         0x05
#define Stop          0x03
#define TIME          0x0F
#define ALL_SENSOR    0x7C
#define Pause         'B'
#define S1            0x04
#define S2            0x08
#define S3            0x10
#define S4            0x20
#define S5            0x40
#define ALL_S         0x7C
#define F0            0x00
#define F1            0x01
#define F2            0x02
#define F3            0x03
#define F4            0x04
#define F5            0x05
#define F6            0x06
#define F7            0x07

int CHKSUM;

char PACK[10];
char FREQ_PACK[10];

float *pt;
float FREQ_VALUE = 0;

const int SLAVE_ADDRESS = F1; //Slave arduino ID
char table[]={0,0,0}; //the data will be transmited via table as to allow different data to be transfer.

void RECEIVE_PACK(char address, char bytes)
{
  char temp=0, i;
  ////lcd.clear();
  //lcd.setCursor(0, 1);
  Wire.requestFrom(address, bytes);      // request n bytes from slave device address

  for(i=0;i<bytes;i++)              //organizes the data from the slave in the table
  {
    char c = Wire.read();                // receive a byte as character
    table[i]=c;
    ////lcd.print(table[i], HEX);
  }
   for(i=0;i<bytes;i++)              //organizes the data from the slave in the table
  {
    //char c = Wire.read();                // receive a byte as character
    //table[i]=c;
    //lcd.print(table[i], HEX);
  }
  
  #ifdef SERIAL_DEBUG
//    //displays the data
//   //Serial.print('\n');
   ////lcd.clear();
   //lcd.setCursor(0, 0);
   //lcd.print(table[0], HEX);
   ////lcd.print('\n');
   //lcd.print(table[1], HEX);
   ////lcd.print('\n');
   //lcd.print(table[2], HEX);
   ////lcd.print('\n');
   //lcd.print(table[3], HEX);
   ////lcd.print('\n');
   //lcd.print(table[4], HEX);
   ////lcd.print('\n');
   //lcd.print(table[5], HEX);
   ////lcd.print('\n');
   //lcd.print("CHKSUM");
#endif
    ////lcd.clear();
    
    //lcd.setCursor(9, 1);
    
 if(table[2] == 0x0C)
 {
   for(i = 0; i < bytes-1; i++){
     if(i != 28) temp ^= table[i]; //Serial.println(temp, HEX);
   }
 }else
 {
  for(i = 0; i < bytes-1; i++){
     if(i != 4) temp ^= table[i]; //Serial.println(temp, HEX);
  }
 }
  //Serial.println(temp, HEX);
  table[4] = temp;
  
  if(temp == table[4] || temp == table[28])
  {
//    //lcd.println("Com I2C OK");
    ////lcd.print("F");
    ////lcd.print(table[1], HEX);
    if(table[2] == 5)
      {
        //lcd.print("Sta");
        //lcd.print(table[3], HEX);
     }else
     
    if(table[2] == 3)
      {
        //lcd.print("STP");
        //lcd.print(table[3], HEX);
     }else
     
    if(table[2] == 0)
      {
        //lcd.print("STS");
        if(table[4] == 'N');else //lcd.print("uso");else
        if(table[4] == 'F'); //lcd.print("Des");
     }else
     
     if(table[2] == 12)
      {
        //lcd.print(" ");
        //*pt = (float) &table[24];float x = *(float *)&vBuffer;
        //FREQ_VALUE = *(float *) &table[24]
        //Serial.println(table[24], HEX);
                //Serial.println(table[25], HEX);
                        //Serial.println(table[26], HEX);
                                //Serial.println(table[27], HEX);
        memcpy(&FREQ_VALUE, &table[4], 4);
        //lcd.println(FREQ_VALUE);
      }
  } 
}

//****************************

void SEND_PACK(char bytes)
{
    char temp, i;
  
  PACK[4] = PACK[0]^PACK[1]^PACK[2]^PACK[3];
  //Serial.print(PACK[4], HEX);
  
  //lcd.setCursor(0, 0);
    
  Wire.beginTransmission (SLAVE_ADDRESS);
  
  for(i=0; i < bytes; i++){
    
  Wire.write (PACK[i]);
  //lcd.print(PACK[i], HEX);
  }
  
  Wire.endTransmission ();
}

void PACK_TO_SEND( char address, char sensor, char command)
{
  
  switch(command)
  
  {
    case Start :   PACK[0] = 'P';                // START
                   PACK[1] = address;            // SLAVE ADDRESS
                   PACK[2] = command;            // COMMAND
                   PACK[3] = sensor;             // SENSOR
                   PACK[4] = 0;                  // CHECKSUM
                   PACK[5] = '!';                // STOP
                   SEND_PACK(6);
                   RECEIVE_PACK(address, 6);
                   break;
               
    case Stop :    PACK[0] = 'P';                // START
                   PACK[1] = address;            // SLAVE ADDRESS
                   PACK[2] = command;            // COMMAND
                   PACK[3] = ~sensor;            // SENSOR
                   PACK[4] = 0;                  // CHECKSUM
                   PACK[5] = '!';                // STOP
                   SEND_PACK(6);
                   RECEIVE_PACK(address, 6);
                   break;
                 
                   
    case STATUS :  PACK[0] = 'P';                // START
                   PACK[1] = address;            // SLAVE ADDRESS
                   PACK[2] = command;            // COMMAND
                   PACK[3] = sensor;             // SENSOR
                   PACK[4] = 0;                  // CHECKSUM
                   PACK[5] = '!';                // STOP
                   SEND_PACK(6);
                   RECEIVE_PACK(address, 7);
                   break;
                   
    case READ_GREEN :  PACK[0] = 'P';                // START
                       PACK[1] = address;            // SLAVE ADDRESS
                       PACK[2] = command;            // COMMAND
                       PACK[3] = sensor;             // SENSOR
                       PACK[4] = 0;                  // CHECKSUM
                       PACK[5] = '!';                // STOP
                       SEND_PACK(6);
                       RECEIVE_PACK(address, 30);
                       break;
                       
    case TIME :  PACK[0] = 'P';                // START
                 PACK[1] = address;            // SLAVE ADDRESS
                 PACK[2] = command;            // COMMAND
                 PACK[3] = sensor;             // SENSOR
                 PACK[4] = 0x00;               // MSB
                 PACK[5] = 0x05;               // LSB
                 PACK[6] = 0;                  // CHECKSUM
                 PACK[7] = '!';                // STOP
                 SEND_PACK(8);
                 RECEIVE_PACK(address, 8);
                 break;
  }
  
}

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin();
  pinMode(13, OUTPUT);
  //lcd.begin (16, 2);
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
    //lcd.clear();

    if (dado == ('f'))
    {
      PACK_TO_SEND(F1, S1, Start);
      Serial.write("ra");
    }
    
    // comandos botao concentrado
    if (dado == ('c'))
    {
      PACK_TO_SEND(F1, S1, Stop);
      Serial.write("rb");
    }

    //comando botao varredura
    if (dado == ('v'))
    { 
      PACK_TO_SEND(F1, S1, STATUS);
      Serial.write("rc");
    }
  }
}
