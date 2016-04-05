
import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray
import sys

from motor import Motor
from distanceSensor import DistanceSensor

class SL1Robot:
  motorA = Motor(9,10)
  motorB = Motor(8,7)
  distanceSensor = DistanceSensor()
  # Distance valirables
  SAFE_DISTANCE = 10.0
  REVERSE_TIME = 0.3
  TURN_TIME = 0.3

  def __init__(self):
    #set variables for the GPIO modes
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

  #TURN all motors off
  def stopMotors(self):
    self.motorA.stopMotors()
    self.motorB.stopMotors()

  #turn BOTH MOTOROS fowards 
  def fowards (self): 
    self.motorA.fowards()
    self.motorB.fowards()

  #turn BOTH MOTOROS backwards
  def backwards (self):
    self.motorA.backwards()
    self.motorB.backwards()

  #turn left
  def right(self):
    self.motorA.backwards()
    self.motorB.fowards()

  #turn left
  def left(self):
    self.motorA.fowards()
    self.motorB.backwards()

  def isNearObstacle(self):
    return self.distanceSensor.measure() < self.SAFE_DISTANCE

  def avoidObstacle(self):
    # Backoff a little:
    self.backwards()
    time.sleep(self.REVERSE_TIME)
    self.stopMotors()
    
    # For now, simply turn:
    self.right()
    time.sleep(self.TURN_TIME)
    self.stopMotors()


