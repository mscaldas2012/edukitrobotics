# CamJam Edukit 3- Robotics - The Object Oriented Way
# Component - Distance Sensor
# This class represents a single distance Sensor used to avoid bumping into obstacles.

import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class DistanceSensor:
    # Define GPIO pins to use on the Pi
    pinTrigger = 17
    pinEcho = 18

    def __init__(self):
        # Set pins as output and input
        GPIO.setup(self.pinTrigger, GPIO.OUT)  # Trigger
        GPIO.setup(self.pinEcho, GPIO.IN)  # Echo
        GPIO.output(self.pinTrigger, False)
        time.sleep(0.1)

    def measure(self):
        # Set trigger to False (Low)
        GPIO.output(self.pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pinTrigger, False)
        startTime = time.time()
        stopTime = startTime
        # The start time is reset until the Echo pin is taken high (==1)
        while GPIO.input(self.pinEcho) == 0:
            startTime = time.time()
            stopTime = startTime

        # Stop when the Echo pin is no longer high - the end time
        while GPIO.input(self.pinEcho) == 1:
            stopTime = time.time()
            # If the sensor is too close to an object, the Pi cannot
            # see the echo quickly enough, so we have to detect that
            # problem and say what has happened.
            if stopTime - startTime >= 0.04:
                print("Hold on There! You're too close for me to see.")
                stopTime = startTime
                break

                # Calculate pulse length
        elapsedTime = stopTime - startTime

        # Distance pulse travelled in that time is
        # time multiplied by the speed of sound (cm/s)
        distance = (elapsedTime * 34326) / 2
        print("Distance: %.1f" % distance)

        return distance
