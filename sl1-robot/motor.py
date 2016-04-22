
# CamJam Edukit 3- Robotics - The Object Oriented Way
# Component - Motor
# This class represents a single motor for the wheels.
# This implementations maintains a constant speed - maximum speed, since it treats the pins as ON/OFF
# For a variable speed motor, check the VariableSpeedMotory.py class.

import RPi.GPIO as GPIO  # Import the GPIO Library
# set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
    def __init__(self, pinFoward, pinBackward):
        self.pinFowards = pinFoward
        self.pinBackwards = pinBackward

        # SET GPIO PIN MODES
        GPIO.setup(self.pinFowards, GPIO.OUT)
        GPIO.setup(self.pinBackwards, GPIO.OUT)

    # Turn motor off
    def stopMotors(self):
        GPIO.output(self.pinFowards, 0)
        GPIO.output(self.pinBackwards, 0)

    # turn MOTOR fowards
    def fowards(self):
        GPIO.output(self.pinFowards, 1)
        GPIO.output(self.pinBackwards, 0)

    # turn  MOTOR backwards
    def backwards(self):
        GPIO.output(self.pinFowards, 0)
        GPIO.output(self.pinBackwards, 1)
