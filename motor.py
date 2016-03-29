# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray

#set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:

  def __init__(self, pinFoward, pinBackward):
    self.pinFowards = pinFoward
    self.pinBackwards = pinBackward

    # SET GPIO PIN MODES
    GPIO.setup(self.pinFowards, GPIO.OUT)
    GPIO.setup(self.pinBackwards, GPIO.OUT)
     
    self.stopMotors()

  #TURN all motors off
  def stopMotors(self):
    GPIO.output(self.pinFowards, 0) 
    GPIO.output(self.pinBackwards, 0) 

  #turn BOTH MOTOROS fowards 
  def fowards (self): 
    GPIO.output(self.pinFowards, 1)
    GPIO.output(self.pinBackwards, 0)

  #turn BOTH MOTOROS backwards
  def backwards (self):
    GPIO.output(self.pinFowards, 0)
    GPIO.output(self.pinBackwards, 1)


