int moterPin = 3;
int moterPin1 = 4;
int moterPin2 = 5;
int moterPin3 = 6;
int moterPin4 = 7;

int strength = 150;



void setup() {
  // put your setup code here, to run once:
  pinMode(moterPin, OUTPUT);
  pinMode(moterPin1, OUTPUT);
  pinMode(moterPin2, OUTPUT);
  pinMode(moterPin3, OUTPUT);
  pinMode(moterPin4, OUTPUT);


  

}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(moterPin, strength);
  analogWrite(moterPin1, strength);
  analogWrite(moterPin2, strength);
  analogWrite(moterPin3, strength);
  analogWrite(moterPin4, strength);


  
}
