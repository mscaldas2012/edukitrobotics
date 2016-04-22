import RPi.GPIO as GPIO

class LineSensor:
  pinLineFollower = 25

  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.pinLineFollower, GPIO.IN)  
    GPIO.setwarnings(False)

  def canSeeLine(self):
    return GPIO.input(self.pinLineFollower) == 0
      
