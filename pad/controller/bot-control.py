from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event0')

KEY_DOWN = 1
KEY_UP = 0
KEY_LB = 310
KEY_RB = 311

def start_stop(event, key, side):
    if event.code == KEY_LB:
        if event.val == KEY_DOWN:
            print("start $side motor")
        if event.val == KEY_UP:
            print("stop $side motor")

for event in gamepad.read_loop():
    start_stop(event, KEY_LB, "left")
    start_stop(event, KEY_RB, "right")


