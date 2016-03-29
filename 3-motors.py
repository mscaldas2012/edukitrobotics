######################################################################################################################
# Camjam edukit 3-robotics
#worksheet 3-motor test code
#####################################################################################################################
import RPi.GPIO as GPIO # Import the GPIO library
import  time # Import the Time Libraray 



####################################################################################################################

#Set the GPIO modes 
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False) 




# Set the GPI0 pin  modes
GPIO.setup (7, GPIO.OUT)	
GPIO.setup (8, GPIO.OUT)
GPIO.setup (9, GPIO.OUT) 
GPIO.setup (10, GPIO.OUT)

#Turn all motors off
GPIO.output(7, 0)
GPIO.output(8, 0)
GPIO.output(9, 0)
GPIO.output(10, 0)

# Turn the right motor fowards
GPIO.output(9, 1)
GPIO.output(10, 0)


# Turn left motor fowards 
GPIO.output(7, 0)
GPIO.output(8, 1)




#####################################################################################################################
# Wait for 1 second 
time.sleep(1)


# Reset the GPIO pins (turns motors off to)
GPIO.cleanup()




######################################################################################################################
 



