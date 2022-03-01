import sys
from motors import motor1
from motors import motor3
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input' + sys.argv[1])

KEY_DOWN = 1
KEY_UP = 0
KEY_LB = 310
KEY_RB = 311
KEY_A = 304
def start_stop(event, key, side):
    if event.code == key:
        if event.value == KEY_DOWN:
            motor1.motorpower(side, motor1.forward)
        if event.value == KEY_UP:
            motor1.motorpower(side, motor1.off)
    if event.code == key:
        if key == 304:
            if event.value == KEY_DOWN:
                motor3.motorpower1(side, motor3.forward)
            if event.value == KEY_UP:
                motor3.motorpower1(side, motor3.off)
for event in gamepad.read_loop():
    print(event)
    start_stop(event, KEY_LB, 0)
    start_stop(event, KEY_RB, 1)
    start_stop(event, KEY_A, 2)
print('Aiden4')

