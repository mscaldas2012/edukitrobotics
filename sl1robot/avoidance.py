# CamJam Edukit 3- Robotics
# Worksheet 4 - Driving and turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # import the time libray
import sys

from SL1Robot import SL1Robot

robot = SL1Robot()

# howNear = 5.0

def main(argv):
  #for step in range (0,4):
  try:
    while True:
      robot.fowards()
      time.sleep(0.1)
      if robot.isNearObstacle():
        robot.stop()
        robot.avoidObstacle()

  except KeyboardInterrupt:
    robot.stop()
    GPIO.cleanup()
    quit()


if __name__ == "__main__":
  main(sys.argv[1:])


