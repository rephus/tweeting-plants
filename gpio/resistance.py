#Tutorials:
#Photocell tutorial: https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
#About analog reading: https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/overview

import RPi.GPIO as GPIO
import time     

class Resistance: 

    _max_time = 200000 # Up to 100 seconds
    def __init__(self,pin):
        GPIO.setmode(GPIO.BOARD)
        self._pin = pin
    
    def _discharge(self):
        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)
        time.sleep(0.1)
    
    def _charge(self):
        measurement = 0
        GPIO.setup( self._pin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input( self._pin) == GPIO.LOW and measurement < self._max_time ):
            measurement += 1
        return measurement
        
    def get(self):
        self._discharge()
        time = self._charge() #Charge time
        #self._time2enum(time)
        return time

    def destroy(self):
        GPIO.cleanup()