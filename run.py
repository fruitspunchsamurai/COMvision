#Field Testing Module
#19/7/13

import RPi.GPIO as GPIO
import time
import os

#Initialise Switch
startpin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(startpin, GPIO.IN)

print “Waiting for output!”

#Loop
while (1):
    if (GPIO.input(startpin)==1):
        os.system(“python /home/pi/sketchbook/ProjectIRIS/FieldTesting/Yellow/Yellowtest.py”)
