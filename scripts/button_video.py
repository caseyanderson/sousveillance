# press and hold to record video

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep

# setup camera and button
camera = PiCamera()
button = Button(4)

# recording flag
is_recording = 0

try:
    # calibrate the camera
    camera.start_preview()
    print("CALIBRATING...")
    sleep(2)
    print("READY TO RECORD!")
    print()

    while True:
        if (button.value == True) and (is_recording == 0):
            print("RECORDING")
            x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
            camera.start_recording('video-' + x + '.mp4')
            is_recording = 1

        if (button.value == False) and (is_recording == 1):
            print("DONE RECORDING!")
            camera.stop_recording()
            is_recording = 0

except KeyboardInterrupt:
    print("INTERRUPTED!")
    button.close()
    camera.close()
