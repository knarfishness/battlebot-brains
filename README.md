# QL BattleBots

For BulletTime 2016-2017, we've constructed and programmed Infrared Combat robots to be used in a customized arena run by a NodeJS server.

## Software Components
1. Main Program (`battlebot.py`): Main Loop of the program, uses all other files as libraries
2. Infrared Control (`infrared.py`): Control for connecting to and using the YS-IRTM Infrared Module
3. PS3 Controller Lib (`ps3.py`): Interface for the `/dev/input/js0` input stream
4. SocketIO Lib (`socket_set.py`): Controller for interacting with the NodeJS SocketIO Game Server
5. Motor Control (`motor_control.py`): Controls the Adafruit PWM DC Motor Shield, forward, back and release functions

## Hardware Components
1. [Raspberry Pi 3 B+ (WiFi, Bluetooth)](https://www.raspberrypi.org/documentation/usage/)
2. [Adafruit Servo / PWM DC Motor shield](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi)
3. [YS-IRTM Infrared Send/Receive module](http://arduino.stackexchange.com/questions/29801/how-to-connect-ir-transmitter-and-receiver-module/29813)
4. [Adafruit large robot chassis](https://learn.adafruit.com/simple-raspberry-pi-robot/overview)
5. Battery Packs (6V AA, 5V USB, eneLoop charger)

## Prerequisites
1. `apt-get update`
2. `apt-get upgrade`
3. `apt-get install python-dev libusb-dev joystick python-pygame`

## PS3 Controller Setup
1. `cd ~`
2. `wget http://www.pabr.org/sixlinux/sixpair.c`
3. `gcc -o sixpair sixpair.c -lusb`
4. `sudo reboot`
5. `sudo ~/sixpair`
6. `sudo bluetoothctl`
7. `discoverable on`
8. `agent on`
9. `connect 38:C0:96:5C:C6:60` (replace with controller address)
10. `trust 38:C0:96:5C:C6:60` (replace with controller address)
11. `jstest /dev/input/js0` (for testing)

## Install this library
1. `git clone https://git/favery/battlebot-brains.git`
2. `cd battlebot-brains`
3. Add the `battlebot.py` script to the startup scripts on the Pi (`/etc/rc.local`)

## Code Customization
1. Set a unique bot ID
2. Bind with a particular controller

## Socket Event Reference
Event | Calls | Description
--- | --- | --- 
connect | `on_connect()` | Connection to the Server
disconnect |  `on_disconnect()`| Event fired when disconnected
reconnect |  `on_reconnect()`| Reconnection event
start |  `on_game_start()`| Game has started (release bot movement, start scoring)
halt |  `on_game_halt()`| Game has been halted (bot hit, other issue?)
resume |  `on_game_resume()`| Game has been resumed (after HALT event)
end |  `on_game_end()`| Game has ended, shut down and score
i_have_been_shot | `i_have_been_shot(id)` | Bot has been shot by provided id

