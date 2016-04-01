# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray
import sys
from random import randint

from motor import Motor
from distanceSensor import DistanceSensor

#set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables for the GPIO monotor pins
motorA = Motor(9,10)
motorB = Motor(8,7)
dist   = DistanceSensor()
#Distance Variables
howNear = 8.0
reverseTime = 0.5
turnTime = 0.3

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


def isNearObstacle(localHowNear):
  d = dist.measure()
  return d < localHowNear;

def avoidObstacle():
  # Back off a little
  backwards()
  time.sleep(reverseTime)
  stopMotors()

  #Turn Rigth
  right()
  time.sleep(turnTime)
  stopMotors()
  time.sleep(1)

def main(argv):
  #for step in range (0,4):
  try:
    while True:
      fowards()
      time.sleep(0.1)
      if isNearObstacle(howNear):
        stopMotors()
        avoidObstacle()

  except KeyboardInterrupt:
    stopMotors()
    GPIO.cleanup()
    quit()


if __name__ == "__main__":
  main(sys.argv[1:])


