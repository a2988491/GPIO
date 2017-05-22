# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
 # BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
 # 输出模式    
GPIO.setup(11, GPIO.OUT)    
try:
    while True:    
        GPIO.output(11, GPIO.HIGH)
        print("on")    
        time.sleep(1)    
        GPIO.output(11, GPIO.LOW) 
        print("out")   
        time.sleep(1) 
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  
