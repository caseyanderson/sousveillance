Note: this information is very similar to the information on [this](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) page.

1. download the compressed raspbian jessie image I prepared for this workshop from [dropbox]() to your computer. when it is done downloading.

2. Download and install the `SDFormatter` from [here](https://www.sdcard.org/downloads/formatter_4/index.html)

3. plug your `microSD` card into an `SD` card adapter and insert into your laptop

4. open `SDFormatter`, which should automatically identify your `SD` card, and select `Overwrite Format`, then click the `Format` button. After a while the application will tell you that it is done erasing all data from the `SD` card

5. with `SD` card plugged in to your computer enter ```diskutil list``` in the terminal to locate the 8GB SD card

    *example output:*

    ```bash
    /dev/disk0 (internal, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:      GUID_partition_scheme                        *500.3 GB   disk0
       1:                        EFI EFI                     209.7 MB   disk0s1
       2:          Apple_CoreStorage HD                      499.4 GB   disk0s2
       3:                 Apple_Boot Recovery HD             650.0 MB   disk0s3
    /dev/disk1 (internal, virtual):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:                  Apple_HFS HD                     +499.0 GB   disk1
                                     Logical Volume on disk0s2
                                     F0EE8AE2-966C-4461-8AB7-DAC4A66164B5
                                     Unencrypted
    /dev/disk2 (internal, physical):
       #:                       TYPE NAME                    SIZE       IDENTIFIER
       0:     FDisk_partition_scheme                        *7.9 GB     disk2
       1:             Windows_FAT_16 RECOVERY                1.2 GB     disk2s1
       2:                      Linux                         33.6 MB    disk2s5
       3:             Windows_FAT_32 boot                    66.1 MB    disk2s6
       4:                      Linux                         6.7 GB     disk2s7
```

3. unmount the sd card, so we can write our new image to it, by entering the following command into the terminal:

    ```bash
    diskutil unmountDisk /dev/disk<disk# from diskutil>
    ```

    *for example:*

    ```bash
    diskutil unmountDisk /dev/disk2
    ```

4. next, copy the data from the uncompress and copy the data from the `.img.gz` file to your SD card by entering the following in the terminal:

    ```bash
gunzip --stdout rasbian.img.gz | sudo dd bs=1m of=/dev/<disk# from diskutil>
    ```

    *for example:*

    ```bash
    gunzip --stdout /Users/mdp/Downloads/2016-05-27-raspbian-jessie.img | sudo dd bs=1m of=/dev/disk2
    ```

    this takes a **VERY LONG TIME**, so go get a cup of coffee or take a walk or something.

5. Eventually you should see something like this in the terminal confirming that `dd` is done writing the`.img` file to the SD card:

    ```bash
    3833+0 records in
    3833+0 records out
    4019191808 bytes transferred in 1642.354445 secs (2447213 bytes/sec)
    ```

6. eject the sd card from your computer with the following command:

    ```bash
    sudo diskutil eject /dev/disk2
    ```

7. put the sd card into your pi, plug power cable in, and confirm that it boots up.
