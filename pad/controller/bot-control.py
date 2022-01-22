from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event9')

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.type == KEY_A:
            if event.val == DOWN:
                print("start left motor")
            if event.val == UP:
                print("stop left motor")
        if event.type == KEY_B:
            if event.val == DOWN:
                print("start right motor")
            if event.val == UP:
                print("stop right motor")

