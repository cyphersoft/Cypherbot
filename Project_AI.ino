#include <Servo.h>

//define right motor control pins
const int rightForward = 8;
const int rightBackward = 9;

//define left motor control pins
const int leftForward = 10;
const int leftBackward = 11;
Servo servo1; 
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6; 
int pos = 150;
void setup()

{

pinMode (rightForward, OUTPUT);
pinMode (rightBackward, OUTPUT);
pinMode (leftForward, OUTPUT);
pinMode (leftBackward, OUTPUT);
servo1.attach(2);
servo2.attach(3); 
servo3.attach(4); 
servo4.attach(5);
servo5.attach(6); 
servo6.attach(7);
Serial.begin(9600);

while (!Serial);

Serial.println("Successful");

}

void loop() {

if (Serial.available())

{

int state = Serial.parseInt();

if (state == 1)

{

digitalWrite(rightForward, HIGH);
digitalWrite(rightBackward,LOW);
digitalWrite(leftForward, HIGH);
digitalWrite(leftBackward, LOW);
Serial.println("Forward");

}
if (state == 2)


{


digitalWrite(rightForward, LOW);
digitalWrite(rightBackward, HIGH);
digitalWrite(leftForward, LOW);
digitalWrite(leftBackward, HIGH);
if (state == 2)

Serial.println("Backward");

}


if (state == 3)


{


digitalWrite(rightForward, LOW);
digitalWrite(rightBackward, LOW);
digitalWrite(leftForward, LOW);
digitalWrite(leftBackward, LOW);
Serial.println("Stop");

}

if (state == 4)
{


digitalWrite(rightForward, LOW);
digitalWrite(rightBackward, HIGH);
digitalWrite(leftForward, HIGH);
digitalWrite(leftBackward, LOW);
Serial.println("Left");


}
if (state == 5)
{


digitalWrite(rightForward, HIGH);
digitalWrite(rightBackward, LOW);
digitalWrite(leftForward, LOW);
digitalWrite(leftBackward, HIGH);
Serial.println("Right");


}
if (state == 5)
{


digitalWrite(rightForward, HIGH);
digitalWrite(rightBackward, LOW);
digitalWrite(leftForward, LOW);
digitalWrite(leftBackward, HIGH);
Serial.println("Right");


}
if (state == 6)
{

servo1.write(160); // Head         
servo2.write(130); //  Hand 
servo3.write(90); // Left Elbow
servo4.write(120); // Right Elbow
servo5.write(90); // Right hand Sholder
servo6.write(140); // Left hand Sholder

}
if (state == 7)
{

       
servo2.write(160); //  Hand 


}

if (state == 8)
{

       
servo2.write(100); //  Hand 


}

if (state == 9)
{


servo5.write(110); // Right hand Sholder
servo6.write(100); // Left hand Sholder

}
if (state ==10)
{


servo5.write(90); // Right hand Sholder
servo6.write(140); // Left hand Sholder


}
}

}
