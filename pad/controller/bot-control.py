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
            print("start $side motor")
        if event.value == KEY_UP:
            print("stop $side motor")
for event in gamepad.read_loop():
    print(event)
    start_stop(event, KEY_LB, "left")
    start_stop(event, KEY_RB, "right")
print('Aiden4')

