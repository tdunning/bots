import RPi.GPIO as GPIO
forward = 1
off = 0
reverse=-1
motor3=0
motor4=1
in1=11
in2=12
in3=15
in4=16
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

def motorpower1(power):
    if power==forward:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
    if power==off:
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
    if power==reverse:
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)

    

