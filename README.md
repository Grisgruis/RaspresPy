Underconstruction...

# RaspresPy #
This is an easy python script for automatic and seamlessly looping of videos managed on [Raspres.com](http://Raspres.com/ "Raspres").

## Why? ##
Because I was so fed up with the fact that is was nearly impossible to put Videos on a Raspberry and start looping them seamlessly without any hassles.

## Features ##
* Mange your videos through an online dashboard on [Raspres.com](http://Raspres.com/ "Raspres"). No more running around with USB-sticks, **free to manage up to 3 Raspberries.**
* Will automatically start looping any video you throw at it.
* Will launch at boot.
* Also supports Presentations (Use Libreoffice - Impress, make sure auto-loop/play is on)

## Setup ##
* Create an account at [Raspres.com](http://Raspres.com/ "Raspres")
* Make sure your Raspberry is setup and is connected to the Internet.
* Open Therminal and run `sudo git clone https://github.com/Grisgruis/RaspresPy.git RaspresPy`
* run `cd RaspresPy`
* run `sudo python install.py`
* Have Patience...
* That's it

Raspres will start running and will show its Mac address which you can add the a device on the [Dashboard](http://Raspres.com/ "Dashboard"). You can assign this device to a group on your account at [Raspres.com](http://Raspres.com/ "Raspres"). When you've uploaded your first video and linked to device to a group, it will automatically start playing the video and start looping.

## Problems? ##
* Make sure your Raspberry has an internet connection.
* No sound support yet, due to the fact `omxplayer --loop` is unable to loop seamlessly.
* Does not support videos within Impress presentations, any ideas are welcome, probably some driver problem.

### Who do I talk to? ###
* Feel free to contact me [chris@smartlaz.com](mailto:chris@smartlaz.com).
