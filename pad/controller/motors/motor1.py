import RPi.GPIO as GPIO
forward = 1
off = 0
reverse=-1
motor1=0
motor2=1
in1=35 
in2=36
in3= 32
in4= 31
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)

def motorpower(motor, power):
    if motor == motor1: 
        if power == forward:
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
        if power == off:
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
        if power == reverse:
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)

    if motor == motor2:
        if power == forward:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
        if power == off:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)
        if power == reverse:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
motorpower(0, off)
motorpower(1, off)
