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

#turn BOTH MOTOROS fowards 
def fowards (): 
  GPIO.output(pinMotorAFowards, 1)
  GPIO.output(pinMotorABackwards, 0)
  GPIO.output(pinMotorBFowards, 1)  
  GPIO.output(pinMotorBBackwards, 0)

#turn BOTH MOTOROS backwards
def backwards ():
  GPIO.output(pinMotorAFowards, 0)
  GPIO.output(pinMotorABackwards, 1)
  GPIO.output(pinMotorBFowards, 0)  
  GPIO.output(pinMotorBBackwards, 1)

#turn left
def right():
  GPIO.output(pinMotorAFowards, 0);
  GPIO.output(pinMotorABackwards, 1)
  GPIO.output(pinMotorBFowards, 1)
  GPIO.output(pinMotorBBackwards, 0)

#turn left
def left():
  GPIO.output(pinMotorAFowards, 1);
  GPIO.output(pinMotorABackwards, 0)
  GPIO.output(pinMotorBFowards, 0)
  GPIO.output(pinMotorBBackwards, 1)




fowards()
time.sleep(1)

stopMotors()
time.sleep(0.2)

left()
time.sleep(0.1)

stopMotors()
time.sleep(0.2)

fowards()
time.sleep(1)

stopMotors() 
time.sleep(0.2)

right()
time.sleep(0.5)

stopMotors() 
time.sleep(0.2)

backwards()
time.sleep(0.5)

stopMotors()

GPIO.cleanup()

