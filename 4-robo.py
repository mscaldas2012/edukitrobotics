# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray
import sys
import motor

#set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables for the GPIO monotor pins
motorA = motor.Motor(9,10)
motorB = motor.Motor(8,7)

#TURN all motors off
def stopMotors():
  motorA.stopMotors()
  motorB.stopMotors()

#turn BOTH MOTOROS fowards 
def fowards (): 
  motorA.fowards()
  motorB.fowards()

#turn BOTH MOTOROS backwards
def backwards ():
  motorA.backwards()
  motorB.backwards()

#turn left
def right():
  motorA.backwards()
  motorB.fowards()

#turn left
def left():
  motorA.fowards()
  motorB.backwards()

def main(argv):
  for step in range (0,4):
    left()
    time.sleep(0.18)
    stopMotors()
    time.sleep(0.1)

    fowards()
    time.sleep(1)
    stopMotors()
    time.sleep(0.2)


if __name__ == "__main__":
  main(sys.argv[1:])

GPIO.cleanup()

