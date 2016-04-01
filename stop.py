# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray

#set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables for the GPIO monotor pins
pinMotorAFowards = 9
pinMotorABackwards = 10
pinMotorBFowards = 8
pinMotorBBackwards = 7

# SET GPIO PIN MODES
GPIO.setup(pinMotorAFowards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBFowards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

#TURN all motors off
def stopMotors():
  GPIO.output(pinMotorAFowards, 0) 
  GPIO.output(pinMotorABackwards, 0) 
  GPIO.output(pinMotorBFowards, 0)
  GPIO.output(pinMotorBBackwards, 0)




stopMotors()
GPIO.cleanup()

