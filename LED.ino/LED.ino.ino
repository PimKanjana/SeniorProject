int data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //initialize serial COM at 9600 baudrate
  pinMode(13, OUTPUT); //make the LED pin (13) as output
  digitalWrite (13, LOW);
  Serial.println("Hi!, I am Arduino");
  Serial.println(Serial.available());

}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available()){
  //Serial.println(Serial.available());

  data = Serial.read();
}

if (data == '1')
digitalWrite (13, HIGH);

else if (data == '0')
digitalWrite (13, LOW);

}
