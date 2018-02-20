void setup() 
{
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(13,OUTPUT);
}

void loop() 
{
  
  // put your main code here, to run repeatedly:
if(Serial.available())
{
  char dado = Serial.read();
  int cont=0;
 // Serial.println(dado);
  
  if (dado == ('f'))
  {
    for (cont;cont<2;cont=cont+1)
    {
    digitalWrite(13,HIGH);
    delay(500);
    digitalWrite(13,LOW);
    delay(500);
    }
    cont=0;
    //Serial.write(" ");
    Serial.println("ra");
    
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
    Serial.println("rb");
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
    Serial.println("rc");
  }
  
   
}
}
