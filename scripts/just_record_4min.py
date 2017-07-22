#!/usr/bin/python3

from picamera import PiCamera
from datetime import datetime
from time import sleep

camera = PiCamera()

x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')

camera.start_preview()
print("CALIBRATING")
sleep(2)
camera.start_recording('/home/pi/' + x + '.h264')
print("RECORDING FIVE SECONDS OF VIDEO")
sleep(240)
print("CAMERA STOPPING")
camera.stop_recording()
camera.close()
