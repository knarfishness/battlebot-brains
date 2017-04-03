# QL BattleBots

For BulletTime 2016-2017, we've constructed and programmed Infrared Combat robots to be used in a customized arena run by a NodeJS server.

## Software Components
1. Python
2. pypi socket.io client
3. Standard Python serial interface

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

## Code Customization
1. Set a unique bot ID
2. Bind with a particular controller

## Socket Event Reference
Event | Calls | Description
--- | --- | --- 
connect | `on_connect()` | Connection to the Server
disconnect |  `on_connect()`| Event fired when disconnected
reconnect |  `on_connect()`| Reconnection event
start |  `on_connect()`| Game has started
halt |  `on_connect()`| Game has been halted
resume |  `on_connect()`| Game has been resumed
end |  `on_connect()`| Game has ended
i_have_been_shot | `i_have_been_shot(id)` | Bot has been shot by provided id

