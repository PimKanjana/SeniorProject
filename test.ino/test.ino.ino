const int pwm = 3 ;  //initializing pin 3 as pwm
const int in_A = 4 ;
const int in_B = 2 ;

//For providing logic to EVO24V9.3 IC to choose the direction of the DC motor 

void setup()
{
pinMode(pwm,OUTPUT) ;   //we have to set PWM pin as output
pinMode(in_A,OUTPUT) ;  //Logic pins are also set as output
pinMode(in_B,OUTPUT) ;
}

void loop()
{
//For Clock wise motion , in_A = High , in_B = Low

digitalWrite(in_B,HIGH) ;
digitalWrite(in_A,LOW) ;
analogWrite(pwm,255) ;


 }
