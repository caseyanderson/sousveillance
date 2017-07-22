##Commands We Used Cheat List

###ssh
secure shell - talk to your rasperry pi

###ssh pi@sous**id**.local
You're logging in as 'pi' to sous**id**.local
Your name is 'pi', and the address is sous**id**.local

###exit
get out of the pi login, back to your home computer's terminal

###cd **directory_name**
change directory

###ls
list contents of directory

###ls -la
list with lots of information and hidden files
-l = long, -a = all

###sudo chmod +x filename.py
change permissions on a file to make it executeable

###ifconfig
lots of internet info

###ifconfig | grep inet
run on your computer to find inet address aka ip address
not the inet6 version
will look something like 192.168.1.96

###rsync **filename_where_you_are** **username**@**destination_ip_address**
remote sync (send files)

###MP4Box -fps 30 -add **video**.h264 **new_name**.mp4
convert the h264 video to a more standard format
this program is on the rasperry pi, run it while logged in there

###Ctrl + c
Bail out! stop the program execution
We used this to stop simple_button.py, ping 

### sudo shutdown now
turn off your raspberry pi (or laptop)
better for the sd card than just yanking the cord

##Git
###git status
see how files have changed from the last git commit
###git pull
sync your files with the repository

##Shortcuts

###tab, tab tab
autocomplete! use in the middle of a command, or after cd.... 
try typing the first letter and hitting tab 1x
try hitting tab 2x in quick succession to see a list - hit tab again to cycle through

###up arrow
scroll through previous commands

###Ctrl + R 
reverse search - type in part of the command from your history

###Command + n
new tab - on Mac Terminal, opens a new tab so you can have your pi connection 
and your own computer terminal open at the same time

###Command + Shift + Side Arrow
Switch between terminal tabs
