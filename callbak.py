# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
 # BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
 # 输出模式    
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
WAIT_TIME = 500
def callbackfunc(channel):
  print("Edge detected on channel %s"%(channel))
  if GPIO.input(11) == GPIO.HIGH:
        print("Button not Pressed")
  if GPIO.input(11) == GPIO.LOW:
        print("Button Pressed")
try:
    GPIO.add_event_detect(11,GPIO.FALLING,callback = callbackfunc,bouncetime = WAIT_TIME)
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 
