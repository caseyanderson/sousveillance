# record 5 seconds of video

from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()

x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')

camera.start_preview()
print("CALIBRATING")
sleep(2)
print("READY")
print()
camera.start_recording('/home/pi/' + x + '.mp4')
print("RECORDING FIVE SECONDS OF VIDEO")
sleep(5)
print("CAMERA STOPPING")
camera.stop_recording()
camera.close()
