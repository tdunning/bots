import RPi.GPIO as GPIO
forward = 1
off = 0
reverse=-1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Motor:
    """a class to control a single motor"""
    pin1 = -1
    pin2 = -2

    def control(self, power):
        if power == forward:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.HIGH)
        if power == off:
            GPIO.output(self.pin1, GPIO.LOW)
            GPIO.output(self.pin2, GPIO.LOW)
        if power == reverse:
            GPIO.output(self.pin1, GPIO.HIGH)
            GPIO.output(self.pin2, GPIO.LOW)

    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)

motors = [Motor(35, 36), Motor(32, 31), Motor(11, 12), Motor(15, 16)]

def motorpower(motor, power):
    motors[motor].control(power)

for i in range(4):
     motorpower(i, off)   
