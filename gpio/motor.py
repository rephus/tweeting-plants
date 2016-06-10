#!/usr/bin/python
import RPi.GPIO as GPIO

#This class is valid for every motor or simple components (only enable and disable) 
#eg: Motors, leds without fade, vibrators, water pumps, even transistors 
class Motor:
    
    def __init__(self, pin):
        self._pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)

    def enable(self):
        GPIO.output(self._pin, True)
        
    def disable(self):
        GPIO.output(self._pin, False)
        
    def destroy(self):
        GPIO.cleanup()