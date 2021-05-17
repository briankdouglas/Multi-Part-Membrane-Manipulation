

double mic = A1;
const int sampleTime = 10; 
double micOut;

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  Serial.print(0);  // To freeze the lower limit
  Serial.print(" ");
  Serial.print(3300);  // To freeze the upper limit
  Serial.print(" ");
  getVoltage();
  //Serial.println(getVoltage());
  //Serial.println(analogRead(mic));
}

double getVoltage()
{
  double maxVoltage = 0;
  double minVoltage = 10000;
  unsigned long startTime= millis();
  while(millis() - startTime < sampleTime) 
   {
      micOut = 5.0*analogRead(mic)/1023*1000;
      if(maxVoltage < micOut)
      {
        maxVoltage = micOut;
      }
      if(minVoltage > micOut)
      {
        minVoltage = micOut;
      }
   }
  
  Serial.print(maxVoltage);
  Serial.print(" ");
  Serial.print(minVoltage);
  Serial.print(" ");
  Serial.println((minVoltage + maxVoltage)/2.0);
  //return maxVoltage;

  //Serial.println(maxVoltage - minVoltage);
}

