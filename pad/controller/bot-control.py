from motors import motor1
from evdev import InputDevice, categorize, ecodes
try:
    gamepad = InputDevice('/dev/input/event0')
except:
    gamepad = InputDevice('/dev/input/event9')

KEY_DOWN = 1
KEY_UP = 0
KEY_LB = 310
KEY_RB = 311
def start_stop(event, key, side):
    if event.code == key:
        if event.value == KEY_DOWN:
            motor1.motorpower(0, motor1.forward)
        if event.value == KEY_UP:
            motor1.motorpower(0, motor1.stop)
for event in gamepad.read_loop():
    print(event)
    start_stop(event, KEY_LB, "left")
    start_stop(event, KEY_RB, "right")
print('Aiden4')

