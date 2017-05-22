#!/usr/bin/python  
import RPi.GPIO as GPIO  
import time 
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(11, GPIO.OUT)  
GPIO.setup(12, GPIO.IN)  
  
def led_on(channel):  
    GPIO.output(11, GPIO.HIGH)  
def led_off(channel):  
    GPIO.output(11, GPIO.LOW)  
try:
#GPIO.add_event_detect(12, GPIO.RISING, callback=led_off, bouncetime=200)  
    GPIO.add_event_detect(12, GPIO.FALLING, callback=led_on, bouncetime=200)
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 
