from microbit import *
steps=0

while True:
    if accelerometer.was_gesture('shake'):
        steps += 2
        display.show(steps)
