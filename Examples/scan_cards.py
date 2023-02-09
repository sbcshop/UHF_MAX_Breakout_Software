#!/usr/bin/python
# Basic exaple to read uhf cards
import spidev as SPI
import mercury

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

buzzer = 17 # connect buzzzer to GPIO17
GPIO.setup(buzzer,GPIO.OUT)    

reader = mercury.Reader("tmr:///dev/ttyS0")
reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")
time.sleep(2)

try:
    while True:
        data=reader.read()
        if(data):
            GPIO.output(buzzer,GPIO.HIGH)
            b = data
            s = str(b)[1:-1]
            x = s.split("(")
            x = x[1].split(")")
            x = x[0]
            x = str(x)[1:-1]
            x = x.lstrip('\'')
            print(x)
            
            time.sleep(0.2)
            
        else:
            GPIO.output(buzzer,GPIO.LOW)
finally:
    GPIO.cleanup()
