import RPi.GPIO as GPIO    
import time
WAIT_TIME = 0.2
previousTime = time.time()        
GPIO.setmode(GPIO.BOARD)        
GPIO.setup(11, GPIO.IN)    
try:
    while True:
        currentTime = time.time()
        if GPIO.input(11) == GPIO.LOW and (currentTime - previousTime) > WAIT_TIME:
            previousTime = currentTime
            print("Button Pressed")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup() 