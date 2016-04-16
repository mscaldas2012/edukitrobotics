import RPi.GPIO as GPIO
import time
from lineSensor import LineSensor

line	 = LineSensor()

try:
  while True:
    if line.isOnLine():
      print('The Sensor is on a black surface, a.k.a., a line')
    time.sleep(0.2)

except KeyboardInterrupt:
   GPIO.cleanup()
