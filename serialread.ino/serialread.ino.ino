const int pwm = 3 ;  //initializing pin 3 as pwm
const int in_A = 4 ;
const int in_B = 2 ;
int data;

void setup() {
  Serial.begin(9600);
  pinMode(pwm,OUTPUT) ;   //we have to set PWM pin as output
  pinMode(in_A,OUTPUT) ;  //Logic pins are also set as output
  pinMode(in_B,OUTPUT) ;
}

void loop() {

while(Serial.available()){
  data = Serial.read();
}
if(data == '1') {
    //For Clock wise motion , in_A = High , in_B = Low
    digitalWrite(in_B,HIGH) ;
    digitalWrite(in_A,LOW) ;
    analogWrite(pwm,55) ;

/*setting pwm of the motor to 255
we can change the speed of rotaion
by chaning pwm input but we are only
using arduino so we are using higest
value to driver the motor  */
/*
    //Clockwise for 3 secs
    delay(300) ;     

    //For brake
    digitalWrite(in_A,HIGH) ;
    digitalWrite(in_B,HIGH) ;
    delay(1000) ;

    //For Anti Clock-wise motion - IN_A = LOW , IN_B = HIGH
    digitalWrite(in_B,LOW) ;
    digitalWrite(in_A,HIGH) ;
    analogWrite(pwm,55);
    delay(300) ;

    //For brake
    digitalWrite(in_A,HIGH) ;
    digitalWrite(in_B,HIGH) ;
    delay(1000) ; */
    } 
else if(data == '0') {
    digitalWrite(in_A,HIGH) ;
    digitalWrite(in_B,HIGH) ;
    delay(1000);
    }
}
