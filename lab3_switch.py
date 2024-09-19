# import the libraries
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

# set the pin numbers to be used from Broadcom chip

xpin = 2
ypin = 3
pushpin = 17
GPIO.setup(xpin, GPIO.IN) # set GPIO pin 4 as Output
GPIO.setup(ypin, GPIO.IN)
GPIO.setup(pushpin, GPIO.IN) # set GPIO pin 17 as Input
#GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # set the initial output of pin 4 to be LOW

while True:
	if (GPIO.input(xpin) == 0 && GPIO.input(ypin) == 0):
		print ("xpin:0, ypin:0, state 0)
		
	print("x:")
	print(GPIO.input(xpin))
	print("y:")
	print(GPIO.input(ypin))
	#GPIO.output(ledpin, not GPIO.input(pushpin)) # read the inverse value of input pin 17
	sleep(0.2)
