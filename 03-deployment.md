### running loop script on startup

There are lots of ways to run a file on startup. Regardless of whether one needs to loop one video forever on boot or loop several videos in a folder forever on boot, its simply a matter of specifying which script (file) one wants to use with `rc.local` (the service which will launch the script on boot):

1. on your pi open `rc.local` with `nano` or `vi`: `sudo nano /etc/rc.local`
2. scroll until you see `exit 0` at the bottom of the file and add two new lines above `exit 0` (`exit 0` has to be the last line in this file)
3. assuming you want to loop all folders in a directory, configure `rc.local` to run `loop_all.sh` with `bash` as a background process  on boot (the `&` at the end of the loop is mission critical here): `./home/cta/videolooper/loop_all.sh &`
4. save and exit
5. reboot: `sudo reboot now`
6. confirm that the looper starts up shortly after the login prompt appears. if not happen make sure `loop_all.sh` has been made executable (`chmod +x loop_all.sh`)
7. since the line in `rc.local` ends with an `&` one can login back into the pi and, among other things, stop the looping process from launching automatically on boot: comment out (add a `#` in front of) the line we just added to `rc.local` in order to revert to non-looping functionality. save, exit, and reboot to confirm non-looping behavior.

alternately, if one wanted to use the `loop_one.sh` script and not `loop_all.sh`, or even to some other `bash` script, one would simply point `rc.local` to `loop_one.sh`, resulting in the following line: `./home/pi/videolooper/loop_one.sh &`
