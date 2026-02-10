import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led  = 26
photo_transistor = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo_transistor, GPIO.IN)
state = 0
while True:
    state = GPIO.input(photo_transistor)
    GPIO.output(led, not state)