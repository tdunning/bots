import RPi.GPIO as GPIO
on = 1
off = 0
motor1=0
motor2=1
in3= 34
in4= 33
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4. GPIO.OUT)


def motorpower(motor, power):
    if motor == motor1: 
        if power == on:
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
        if power == off:
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
    if motor == motor2:
        if power == on:
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.HIGH)
        if power == off:
            GPIO.output(in4, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
