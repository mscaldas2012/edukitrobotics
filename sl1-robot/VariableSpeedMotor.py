# CamJam Edukit 3- Robotics - The Object Oriented Way
# Component - Motor
# This class represents a single motor for the wheels.It allows the motor to have variable speeds

# File created on 4/19/16
# Author: Marcelo Caldas - mscaldas@gmail.com
#


# CamJam Edukit 3- Robotics - The Object Oriented Way
# Component - Motor
# This class represents a single motor for the wheels.

import RPi.GPIO as GPIO  # Import the GPIO Library
# set variables for the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class VariableSpeedMotor:
    freq = 20
    dutyCycle = 50
    stop = 0

    def __init__(self, pinFoward, pinBackward):
        self.pinFowards = pinFoward
        self.pinBackwards = pinBackward

        # SET GPIO PIN MODES
        GPIO.setup(self.pinFowards, GPIO.OUT)
        GPIO.setup(self.pinBackwards, GPIO.OUT)

        self.pwmPinFowards = GPIO.PWM(self.pinFowards, self.freq)
        self.pwmPinBackwards = GPIO.PWM(self.pinBackwards, self.freq)
        self.pwmPinFowards.start(self.stop)
        self.pwmPinBackwards.start(self.stop)

    # Turn motor off
    def stopMotors(self):
        self.pwmPinFowards.ChangeDutyCycle(self.stop)
        self.pwmPinBackwards.ChangeDutyCycle(self.stop)

    # turn MOTOR fowards
    def fowards(self):
        self.pwmPinFowards.ChangeDutyCycle(self.dutyCycle)
        self.pwmPinBackwards.ChangeDutyCycle(self.stop)

    # turn  MOTOR backwards
    def backwards(self):
        self.pwmPinFowards.ChangeDutyCycle(self.stop)
        self.pwmPinBackwards.ChangeDutyCycle(self.dutyCycle)

    def changeSpeed(self, howMuch):
        if (howMuch > 0):
            self.dutyCycle = min(self.dutyCycle + howMuch, 100)
        else:
            self.dustyCycle = max(self.dutyCycle - howMuch, 0)

