const int pwm = 3 ;  
const int in_A = 4 ;
const int in_B = 2 ;
int data;

void setup()
{
pinMode(pwm,OUTPUT) ;   //we have to set PWM pin as output
pinMode(in_A,OUTPUT) ;  //Logic pins are also set as output
pinMode(in_B,OUTPUT) ;
Serial.begin(9600);
}

void loop() 
{ 
    if (Serial.available() > 0) {
        Serial.println("Hi");
        data = Serial.read();
        // here '1' (the character) is important as 1 is the number
        // and '1' equals 0x31 (ASCII)
        if(data == '1') {   
            digitalWrite(in_B,HIGH) ;
            digitalWrite(in_A,LOW) ;
            analogWrite(pwm,255) ;
            delay(30) ;  
        } else if(data == '0') {
            digitalWrite(in_A,HIGH) ;
            digitalWrite(in_B,HIGH) ;
            delay(10) ;
        }
    }
}
