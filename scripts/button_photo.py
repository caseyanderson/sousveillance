# still photo taken at every button press

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from time import sleep

button = Button(4)
camera = PiCamera()

def capture():
    x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
    print("taking photo")
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/' + x + '.jpg')
    print("saving photo")
    camera.stop_preview()
    print("DONE!")
    print()

try:
    while True:
        button.when_pressed = capture
except KeyboardInterrupt:
    print("INTERRUPTED!")
    button.close()
    camera.close()
