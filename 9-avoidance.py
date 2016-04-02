# CamJam EduKit 3 - Robotics
# Worksheet 9 - Obstacle Avoidance 

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define GPIO pins to use Pi
pinTrigger = 17
pinEcho = 18


# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# Settng the duty cycle to 0 means the motors will not turn
Stop = 0
# set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#set variables for the GPIO motor pins
pinMotorAFowards = 9
pinMotorABackwards = 10
pinMotorBFowards = 8
pinMotorBBackwards = 7
#Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

# how may times to turn the pin on and off each second
Frequency = 20
#how long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# setting the duty cycle to 0 means the motor will not turn
Stop = 0
 
# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAFowards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBFowards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


# sistance variables
HowNear = 5.0
ReverseTime = 0.5
TurnTime = 0.75

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAFowards = GPIO.PWM(pinMotorAFowards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBFowards = GPIO.PWM(pinMotorBFowards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAFowards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBFowards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
    pwmMotorAFowards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBFowards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Fowards():
    pwmMotorAFowards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBFowards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def Backwards():
    pwmMotorAFowards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBFowards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Right():
    pwmMotorAFowards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBFowards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Left():
    pwmMotorAFowards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBFowards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

def IsNearObstacle(localHowNear):
  Distance = Measure()
  print("IsNearOsbtacle: "+str(Distance))
  if Distance < localHowNear:
    return True
  else:
    return False

def Measure():
  GPIO.output(pinTrigger, True)
  time.sleep(0.00001)
  GPIO.output(pinTrigger, False)
  StartTime = time.time()
  StopTime = StartTime

  while GPIO.input(pinEcho)==0:
    StartTime = time.time()
    StopTime = StartTime

  while GPIO.input(pinEcho)==1:
    StopTime = time.time()
    if StopTime-StartTime >=0.04:
      print ("Hold on there")
      StopTime = StartTime
      break


  ElapsedTime = StopTime-StartTime
  Distance = (ElapsedTime * 34326)/2
  return Distance
   

def AvoidObstacle():
  Backwards()
  time.sleep(ReverseTime)
  StopMotors()

  Right()
  time.sleep(TurnTime)
  StopMotors()


try:
  GPIO.output(pinTrigger, False)
  time.sleep(0.1)
#  time.sleep(1)
  while True:
    Fowards()
    time.sleep(0.1)
    if IsNearObstacle(HowNear):
      StopMotors()
      AvoidObstacle()		
except KeyboardInterrupt:
   StopMotors()
   GPIO.cleanup()
