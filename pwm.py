import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 10)
try:
    while True:
        p.start(90)
#input('Press return to stop:')   # use raw_input for Python 2
except KeyboardInterrupt:
    p.stop()
finally:
    GPIO.cleanup()

