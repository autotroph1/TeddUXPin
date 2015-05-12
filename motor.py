import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(23,GPIO.OUT)  # mouth
GPIO.setup(24,GPIO.OUT)  # ears
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)


while(True):
        GPIO.output(23,True)
        GPIO.output(24,False)
        time.sleep(0.5)
        GPIO.output(23,False)
        GPIO.output(24,True)
        time.sleep(0.5)

