### looping a video file

omxplayer player has built-in looping functionality: `omxplayer --loop nyan_cat.mp4`

omxplayer also has a bunch of parameters to customize the specifics of the loop playback. try running the following (replace `nyan_cat.mp4` with whatever your video is called): `omxplayer -b --loop --no-osd -o hdmi nyan_cat.mp4`

more specifically:

* `-b`: forces omxplayer to create a black background behind the video
* `--loop`: the normal command to force omxplayer to loop a video file
* `--no-osd`: hides the on-screen dialogue messages (like "Seeking..." when looping back to the beginning of the video)
* `-o hdmi`: forces audio output via the HDMI cable
* `-r`: not used in the command above but can force the video to fill the screen


### looping one video forever

With minimal alterations, and a bit of setup, one can make a `bash` file that runs the omxplayer loop command:

1. on your raspberry pi make a folder called `videolooper` in your `home` directory: `mkdir videolooper`
2. cd into `videolooper`: `cd videolooper`
3. make a `video` folder inside `videolooper` (videos will be stored here): `mkdir video`
4. on your mac make a new file called `loop_one.sh` wherever you want (we are going to set this up and then send it to the raspberry pi via `scp`): `touch loop_one.sh`
5. open up `loop_one.sh` in whatever text editor you like (remember, we are still on our mac at this point). i like [Atom](https://atom.io/) : `atom loop_one.sh`
6. Copy the following code and paste it all into your `loop_one.sh` file (then save and exit):

    ```bash
    #!/bin/sh

    omxplayer -b --loop --no-osd -o hdmi /home/pi/nyan_cat.mp4

    ```
7. use `scp` to send `loop_one.sh` to your raspberry pi (note, this requires knowledge of your pi's ip address): `scp loop_one.sh pi@<PI_IP_ADDRESS>:/home/pi/`

8. back on your pi, make `loop_one.sh` executable with `chmod`: `chmod +x loop_one.sh`
9. run `loop_one.sh` with the following command `./loop_one.sh`
10. `Control-C` (KeyboardInterrupt) to exit loop


### looping all videos in a playlist forever

1. on your mac make a new file called `loop_all.sh`: `touch loop_all.sh`
2. open it with your preferred text editor  (again, I use Atom so it looks like this when I do it): `atom loop_all.sh`
3. Copy the code from [this](https://github.com/caseyanderson/rpi/blob/master/02_VideoLooper/loop_scripts/loop_all.sh) file and paste it all into your `loop_all.sh` file (then save and exit)
4. send `loop_all.sh` to your raspberry pi: `scp loop_all.sh pi@<PI_IP_ADDRESS>:/home/pi/`
5. move the file into the `videolooper` directory: `mv loop_all.sh videolooper/loop_all.sh`
6. update `loop_all.sh` to include the correct path and filename information (via `nano` or `vi`) stored at `VIDEOPATH`
7. make `loop_all.sh` executable with `chmod`: `chmod +x loop_all.sh`
8. run `loop_all.sh` with the following command `./loop_all.sh`
9. `Control-C` (KeyboardInterrupt) to exit loop
