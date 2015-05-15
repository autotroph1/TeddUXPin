import RPi.GPIO as GPIO
import time
import subprocess

try:
    while(True):
        open = subprocess.Popen(['./myprog','1','0'])
        open.wait()
        close = subprocess.Popen (['./myprog','1','1'])
        close.wait()
finally:
        subprocess.Popen(['./myprog','1','1'])
