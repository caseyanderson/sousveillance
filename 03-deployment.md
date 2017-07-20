### running scripts on startup

There are lots of ways to run a file on startup. Regardless of what kind of job one wants to give to a pi on boot, it's simply a matter of specifying which `script` (`file`) one wants to use with `rc.local` (the service which will launch the script on boot):

1. make `button_led_video.py` executable: `sudo chmod +x button_led_video.py`
2. open `rc.local`: `sudo nano /etc/rc.local`
3. scroll down (using the arrow keys) until you see `exit 0` at the bottom of the file and add two new lines above `exit 0` (`exit 0` **has** to be the **last line in this file**)
4. copy and paste this command into the empty space you created in the previous step: `su -c "python3 /path/to/file.py" pi &`
5. save and exit
6. reboot: `sudo reboot now`
7. confirm that the picamera starts up shortly after the login prompt appears
8. since the line in `rc.local` ends with an `&` one can login back into the pi and, among other things, stop the file from running. simply comment out (add a `#` in front of) the line we just added to `rc.local` in order to revert to non-looping functionality. save, exit, and reboot to return to normal functionality
