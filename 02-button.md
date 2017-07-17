## button

### reference
* [gpiozero docs](https://gpiozero.readthedocs.io/en/stable/)
* [Getting started with physical computing](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/)


### equipment

### hookup pattern

Note: Illustrations sourced from [here](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/).

<img src="/assets/button.png" width="630" height="375">


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

```
