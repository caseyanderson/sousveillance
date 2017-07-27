## picamera

### reference
* [getting started with pi camera](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)
* [pi camera docs](https://picamera.readthedocs.io/en/release-1.13/)
* Andrea Fabrizi's [dropbox uploader](https://github.com/andreafabrizi/Dropbox-Uploader)
* [GPAC](https://gpac.wp.imt.fr/mp4box/mp4box-documentation/)


### equipment
* [pi camera](https://www.adafruit.com/product/3099)
* [pi camera adapter](https://www.adafruit.com/product/3157) (if using the pi zero w)


### connecting the picamera

Connect your PiCamera to the Camera Cable and then to the Pi Zero W. It should look like this (photo sourced from Adafruit):

<img src="/media/pizero_hookup_example.jpeg" width="485" height="364">


### simple video

Below one can find the code to capture video via Python3 with the PiCamera:

```python
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
camera.start_recording('/home/pi/' + x + '.h264')
print("RECORDING FIVE SECONDS OF VIDEO")
sleep(5)
print("CAMERA STOPPING")
camera.stop_recording()
camera.close()
```

A few quick notes:

* we allow the camera to calibrate for 2 seconds after calling `camera.start_preview()`, which gives the camera time to focus
* `camera.capture()` is replaced here with `camera.start_recording()`, which will record video until we issue the stop command (`camera.stop_recording()`). Note that the `datetime` line from [simple_photo](https://github.com/caseyanderson/sousveillance/blob/master/scripts/simple_photo.py) is reused verbatim here to avoid overwriting files/provide a timeline via filename
* the `sleep` command controls how long the video is, so recording video longer than five seconds is simply a matter of increasing the sleep time to the desired duration


### converting video

Note: mad props to [this](http://www.raspberrypi-spy.co.uk/2013/05/capturing-hd-video-with-the-pi-camera-module/) article for the conversion process.

[simple_video](https://github.com/caseyanderson/rpi/blob/master/03_Camera/camera_scripts/simple_video.py) saves video as Raw H264 Video Data, so there are some extra steps to take prior to being able to view it without plugging a display into our Pi:

1. Download and install `gpac`: `sudo apt-get install -y gpac`
2. `cd` to the directory where your video lives and, using `MP4Box` (installed with `gpac`), convert your video to `.mp4` by editing (to suit your needs) and then execute this command: `MP4Box -fps 30 -add myvid.h264 myvid.mp4`
3. once the video has been converted, delete the original: `rm mywid.h264`
4. finally `cd` to the `Dropbox-Uploader` folder, edit (to suit your needs) and then execute the following command: `./dropbox_uploader.sh upload ./myvid.mp4 /`
5. back on your Macbook navigate to your dropbox folder and double click the `.mp4` to watch


#### viewing video (dropbox sync)

This method relies on Andrea Fabrizi's [dropbox uploader](https://github.com/andreafabrizi/Dropbox-Uploader).

1. on your Pi run the following command to clone the dropbox uploader repo: `git clone https://github.com/andreafabrizi/Dropbox-Uploader.git`
2. next on your Macbook navigate to dropbox and, if you do not already have one, set up a free account.
3. once you have a dropbox account setup, go [here](https://www.dropbox.com/developers/apps) to setup an application to interact with dropbox
4. this next part will probably change from time-to-time, but as of 7/18/2017 the process was as follows:
    * click  the `Create app` button
    * select “Dropbox API” and “Full Dropbox,” give your app a unique name (example: yourname_camera_app) then confirm by clicking `Create the app`
    * finally, in the settings tab there is a button that reads `Generate access token`. Click this button and then copy the string of seemingly random letters and numbers (referred to as a token) to your clipboard <CMD+C>. This string is how dropbox will identify your raspberry pi
5. back on the raspberry pi `cd` into the `Dropbox-Uploader` folder and make `dropbox_uploader.sh` executable by running the following: `sudo chmod +x dropbox_uploader.sh`
6. next run the `bash` script: `./dropbox_uploader.sh`
7. you will be prompted to enter your access token, which should still be in your clipboard, so paste (<CMD+V>) it into the terminal and type `y` to confirm
8. try uploading the `README.md` file in the `Dropbox-Uploader` folder to dropbox to confirm functionality: `./dropbox_uploader upload README.md /`
9. If successful, you should see something like the following in the terminal: ` > Uploading "/home/cta/Dropbox-Uploader/README.md" to "/README.md"... DONE`
10. back on your Macbook navigate to dropbox to confirm that `README.md` is there

To upload photos simply edit this command to suit your needs: `./dropbox_uploader.sh upload fileorfoldertoupload /`. Notes to keep in mind:

* you have to be in the `Dropbox-Uploader` directory for this command to work
* that the trailing `/` is an important part of this command
* this command works for single files as well as a directory full of files
