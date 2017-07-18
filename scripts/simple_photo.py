#!/usr/bin/python3

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')

camera.start_preview()
sleep(2)
camera.capture('/home/pi/' + x + '.jpg')
camera.stop_preview()
camera.close()
