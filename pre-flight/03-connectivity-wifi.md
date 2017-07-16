### WiFi

There is one file that needs to be configured to setup WiFI on the Raspberry Pi: `/etc/wpa_supplicant/wpa_supplicant.conf`.

1. Connect to the Raspberry Pi via `FTDI`
2. Navigate to `/etc/wpa_supplicant/wpa_supplicant.conf`: `cd /etc/wpa_supplicant/`
3. Open `wpa_supplicant.conf` with `nano`: `sudo nano wpa_supplicant.conf` and move on to the next sequence (Configuring wpa_supplicant)


### Configuring wpa_supplicant

Here is what `wpa_supplicant` would look like with only one network (with nonsense credentials):

```bash

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
   ssid="WIFINETWORKNAME"
   psk="WIFINETWORKPASSWORD"
}
```

To configure it for a your network simply insert the WiFi network name in `ssid` and the password in `psk`. Note that you have to use quotes for both of these fields. Save changes, exit, and reboot to confirm that you can connect to the network after logging back in.
