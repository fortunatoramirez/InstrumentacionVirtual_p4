int analogPinA0 = A0;
int val = 0;
//float valFloat = 0;

void setup(){
  Serial.begin(9600);
  analogReadResolution(10);
}

void loop(){
  
  if(Serial.read() == 's'){
    val = analogRead(analogPinA0);
    Serial.println(val);
    //valFloat = ((float)val/1023)*5;
    //Serial.println(valFloat);
    
  }

}
