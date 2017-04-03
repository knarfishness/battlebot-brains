
// obstacle avoidance code
// by: knarfishness
// on: 2/7/2017
#include <AFMotor.h> // Motor Shield Lib

#define trigPin A4 // Ultrasonic Pins
#define echoPin A5 

AF_DCMotor motor1(3,MOTOR12_64KHZ); // set up motors.
AF_DCMotor motor2(2, MOTOR12_64KHZ);
 
void setup() {
  Serial.begin(9600); // begin serial communitication  
  pinMode(trigPin, OUTPUT);// set the trig pin to output (Send sound waves)
  pinMode(echoPin, INPUT);// set the echo pin to input (recieve sound waves)
  motor1.setSpeed(125); //set the speed of the motors, between 0-255
  motor2.setSpeed (105);  
}
 
void loop() {

   long duration, distance; // start the scan
  digitalWrite(trigPin, LOW);  
  delayMicroseconds(2); // delays are required for a succesful sensor operation.
  digitalWrite(trigPin, HIGH);

  delayMicroseconds(10); //this delay is required as well!
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;// convert the distance to centimeters.
  
  if (distance < 25)/*if there's an obstacle 25 centimers, ahead, do the following: */ {   
   Serial.println ("Close Obstacle detected!" );
    Serial.println ("Obstacle Details:");
Serial.print ("Distance From Robot is " );
Serial.print ( distance);
Serial.print ( " CM!");// print out the distance in centimeters.

Serial.println (" The obstacle is declared a threat due to close distance. ");
Serial.println (" Turning !");
    motor1.run(FORWARD);  // Turn as long as there's an obstacle ahead.
    motor2.run (BACKWARD);

}
  else {
   Serial.println ("No obstacle detected. going forward");
   delay (15);
   motor1.run(FORWARD); //if there's no obstacle ahead, Go Forward! 
    motor2.run(FORWARD);  
  }  
  
  

  
  
  
 
}