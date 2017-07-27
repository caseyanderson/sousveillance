## button

### reference
* [gpiozero docs](https://gpiozero.readthedocs.io/en/stable/)
* [Getting started with physical computing](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/)


### equipment
* SPST Button
* Breadboard


### hookup pattern

Note: Illustrations sourced from [here](https://www.raspberrypi.org/learning/physical-computing-with-python/worksheet/).

<img src="/media/button.png" width="630" height="375">


### simple button

Using a button to print one of two messages to the terminal can be achieved simply with the following:

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

#### recording video

One can use the button as a trigger to record video for arbitrary durations. Here we look at two variables to determine whether the video should start recording or not:

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
