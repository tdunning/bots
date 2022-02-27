import motor1.py

while True:
    motorpower(0, 0)
    motorpower(1, 0)
    sleep(0.5)

    motorpower(0, 1)
    motorpower(1, 1)
    sleep(0.5)

    motorpower(0, 0)
    motorpower(1, 0)
    sleep(0.5)

    motorpower(1, 1)
    motorpower(0, 1)