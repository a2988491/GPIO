# -*- coding: utf-8 -*-    
import RPi.GPIO as GPIO    
import time    
 # BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)    
 # 输出模式    
GPIO.setup(11, GPIO.IN)
a = 0.2
previousTime = time.time()
try:    
    while True:
        currentTime = time.time()
    	if GPIO.input(11) == GPIO.LOW and (currentTime - previousTime) > a :
             previousTime = currentTime
             print("BUTTON PRESSED")
except KeyboardInterrupt:
    print("GGG")
finally: 
    GPIO.cleanup()  
