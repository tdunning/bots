from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event9')

KEY_DOWN = 1
KEY_UP = 0

def start_stop(event, key, side):
    if event.type == key:
        if event.val == KEY_DOWN:
            print("start $side motor")
        if event.val == KEY_UP:
            print("stop $side motor")

for event in gamepad.read_loop():
    start_stop(event, KEY_A, "left")
    start_stop(event, KEY_B, "right")


