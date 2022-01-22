from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event9')

def start_stop(event, key, side):
    if event.type == key:
        if event.val == DOWN:
            print("start $side motor")
        if event.val == UP:
            print("stop $side motor")

for event in gamepad.read_loop():
    start_stop(event, KEY_A, "left")
    start_stop(event, KEY_B, "right")


