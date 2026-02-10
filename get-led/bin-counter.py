import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds  = [24, 22, 23, 27, 17, 25, 12, 16][::-1]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
period = 0.2
num = 0
up = 9
down = 10
GPIO.setup(up, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)

def decTObin(a):
    return [int(i) for i in bin(a)[2:].zfill(8)]

while True:
    if GPIO.input(up):
        num += 1
        if num > 255: 
            num = 255
        print(num, decTObin(num))
        GPIO.output(leds, decTObin(num))
        time.sleep(period)
    if GPIO.input(down):
        num -= 1
        if num < 0: 
            num = 0
        print(num, decTObin(num))
        GPIO.output(leds, decTObin(num))
        time.sleep(period)