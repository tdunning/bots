from evdev import InputDevice, categorize, ecodes
try:
    gamepad = InputDevice('/dev/input/event0')
except:
    gamepad = InputDevice('/dev/input/event9')
print('Aiden1')

KEY_DOWN = 1
KEY_UP = 0
KEY_LB = 310
KEY_RB = 311
print('Aiden2')
def start_stop(event, key, side):
    if event.code == KEY_LB:
        if event.val == KEY_DOWN:
            print("start $side motor")
        if event.val == KEY_UP:
            print("stop $side motor")
print('Aiden3')
for event in gamepad.read_loop():
    print('event')
    print('aiden:eventval', event.val , '  event code =', event.code)
    start_stop(event, KEY_LB, "left")
 #   start_stop(event, KEY_RB, "right")
print('Aiden4')

