#!/usr/bin/python3
# press and hold to record video

from gpiozero import Button
from gpiozero import LED
from picamera import PiCamera
from datetime import datetime
from time import sleep

# setup led and button
button = Button(4)
led = LED(17)

# recording flag
is_recording = 0

try:

    while True:
        if (button.value == True) and (is_recording == 0):

            camera = PiCamera()
            sleep(2)
            camera.start_preview()
            print("CALIBRATING...")
            print("READY TO RECORD!")
            print()
            print("RECORDING")
            x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
            path = ''.join(['/home/pi/', x, '.h264'])
            camera.start_recording(path)
            is_recording = 1
            led.on()

        elif (button.value == False) and (is_recording == 1):
            print("DONE RECORDING!")
            camera.stop_recording()
            camera.stop_preview()
            led.off()
            camera.close()
            is_recording = 0


except KeyboardInterrupt:
    print("INTERRUPTED!")
    button.close()
    camera.close()
    led.close()
