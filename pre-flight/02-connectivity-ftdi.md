### FTDI Breakout

Download and install the FTDI Driver to your laptop from  [here](http://www.ftdichip.com/Drivers/VCP/MacOSX/FTDIUSBSerialDriver_v2_3.dmg).

With with your RPi off, make the following connections between a [FTDI Basic Breakout](https://www.sparkfun.com/products/9873) and the Raspberry Pi:

photo of raspberry pi with  here

While any FTDI breakout should work, note that the logic levels of the Raspberry Pi are `3.3V,` so you must use either a `3.3V` FTDI device or a `5V` to `3.3V Logic Level Converter` will also be needed). Interfacing with the Raspberry Pi `GPIO` is much easier if one uses something like the Adafruit [PiCobbler](https://www.adafruit.com/products/914) or Sparkfun [Pi Wedge](https://www.sparkfun.com/products/13717) (which already has a built in spot for the FTDI breakout board).

After double-checking your connections, plug the Raspberry Pi power adapter into its port and connect the other end to an outlet.


#### Connecting via screen

1. On your host CPU, open a new terminal window and type the following command to connect to your Pi's console: `screen /dev/tty.usbserial<TAB> `. You should see the terminal autocomplete with some identifier of some sort. For example, after hitting tab the command looks like this on my CPU: `screen /dev/tty.usbserial-AH02LSSH`
2. Add the `BAUD` rate (`115200`) to the command above (the command should like something like this: `screen /dev/tty.usbserial-AH02LSSH 115200`). Press enter to issue the command
3. Once a connection is made you should notice that your terminal label will update to `screen` as opposed to `bash`. Press enter to bring up the login screen
4. Enter login credentials


#### Disconnecting via screen

1. Type `exit` and then hit enter to return to the login prompt
2. Open a new terminal tab
3. We need to get the ID number of the screen session so we can kill it. Enter `screen -ls` in the terminal and copy the number before `.tty001` for use in the next step
4. Issue the following command in the terminal: `screen -X -S <SESSION NUMBER> quit`
