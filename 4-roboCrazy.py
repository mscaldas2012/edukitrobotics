# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray
import sys
from random import randint

from motor import Motor

#set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables for the GPIO monotor pins
motorA = Motor(9,10)
motorB = Motor(8,7)

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
  try:
    directions = {0: fowards,
                  1: backwards,
                  2: left,
                  3: right}
    while True:
      dir = randint(0,3)
      directions[dir]()
      time.sleep(1)
      stopMotors()
      time.sleep(0.2)
  except KeyboardInterrupt:
    GPIO.cleanup()
    quit()

if __name__ == "__main__":
  main(sys.argv[1:])


