#include <Servo.h>

// Define pins for L298N (Back Wheels)
const int ENA = 9;  // PWM pin for speed control
const int IN1 = 7;  // Direction control 1
const int IN2 = 8;  // Direction control 2
Servo myservo;      // Create servo object to control a servo
int pos = 30;        // Variable to store the servo position

void setup() {
  Serial.begin(9600); // Initialize Bluetooth communication
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  myservo.attach(3); // Attach the servo on pin 3
  myservo.write(30); // Center the servo initially
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "FORWARD") {
      moveForward();
    } else if (command == "BACKWARD") {
      moveBackward();
    } else if (command == "LEFT") {
      turnLeft();
    } else if (command == "RIGHT") {
      turnRight();
    } else if (command == "STOP") {
      stopMotors();
    } else if (command == "CENTER") {
      centerWheel();  // New command to center the wheel
    }
  }
}

void moveForward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 200);
}

void moveBackward() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, 230);
}

void turnLeft() {
  for (pos = 0; pos <= 60; pos += 5) {
    myservo.write(pos);
    delay(10);
  }
}

void turnRight() {
  for (pos = 60; pos >= 0; pos -= 5) {
    myservo.write(pos);
    delay(10);
  }
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);
}

void centerWheel() {
  // Move the servo to the center position
  myservo.write(30);  // Center position
  stopMotors();       // Stop the motors as well
}

