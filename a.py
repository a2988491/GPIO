# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
 # BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
 # 输出模式    
GPIO.setup(11, GPIO.IN)    
def callbackfunc(channel):
    print("Button Pressed")
try:
    GPIO.add_event_detect(11,GPIO.RISING,callback = callbackfunc,bouncetime = 500)
    while True:
        time.sleep(20)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 