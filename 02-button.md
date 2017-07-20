## button

### reference
* [gpiozero docs](https://gpiozero.readthedocs.io/en/stable/)
* [Getting started with physical computing](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/)


### equipment

### hookup pattern

Note: Illustrations sourced from [here](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/).

<img src="/media/button.png" width="630" height="375">


### simple button

The gpiozero module provides lots of nice convenience methods. For example, using a button to print one of two messages to the terminal can be achieved simply with the following:

```python
from gpiozero import Button

button = Button(4)

try:
    while True:
        if button.is_pressed:
            print("Button is pressed")
        else:
            print("Button is not pressed")
except KeyboardInterrupt:
    print("interrupted!")
    button.close()

```


### button + pi camera

#### still photos

In the code below button input is used to trigger a `camera.capture()` statement from the `picamera` module, effectively turning the raspberry pi into a point-and-shoot camera. Note the `capture()` function here, which is trigged by `button.when_pressed()`

```python
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

```


#### recording video

With some alterations to [button_camera_still.py](https://github.com/caseyanderson/rpi/blob/master/05_GPIO/02_button/scripts/button_camera_still.py)  one can use the button as a trigger to record video for arbitrary durations. Here we look at two variables to determine whether the video should start recording or not:
1. whether the button was pressed or not (where `True` means the button has been pressed)
2. a variable storing the state of the video recording (`is_recording`)

In other words, if `button.value()` returns `True` and `is_recording` is set to `0`, `camera.start_recording()` starts, continuing until both `button.value()` returns `False` while `is_recording` is still set to `1`. The inclusion of `is_recording` is a kind of safety mechanism here and in a sense makes our test "smarter" (or slightly less error prone). Calibration happens automatically at the top of the `try` statement, and the `datetime.now().strftime()` line allows one to repeatedly record video with no chance of accidentally overwriting previous files.


```python
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

```


### converting video

Note: mad props to [this](http://www.raspberrypi-spy.co.uk/2013/05/capturing-hd-video-with-the-pi-camera-module/) article for the conversion process.

[simple_video](https://github.com/caseyanderson/rpi/blob/master/03_Camera/camera_scripts/simple_video.py) saves video as Raw H264 Video Data, so there are some extra steps to take prior to being able to view it without plugging a display into our Pi:

1. Download and install `gpac`: `sudo apt-get install -y gpac`
2. `cd` to the directory where your video lives and, using `MP4Box` (installed with `gpac`), convert your video to `.mp4` by editing (to suit your needs) and then execute this command: `MP4Box -fps 30 -add myvid.h264 myvid.mp4`
3. once the video has been converted, delete the original: `rm mywid.h264`
4. finally `cd` to the `Dropbox-Uploader` folder, edit (to suit your needs) and then execute the following command: `./dropbox_uploader.sh upload ./myvid.mp4 /`
5. back on your Macbook navigate to your dropbox folder and double click the `.mp4` to watch
