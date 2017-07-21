#!/usr/bin/env python

# handle imports
import time
import serial
import string

# handle libraries
# from libraries.ps3 import *
# from libraries.motor_control import *
# from libraries.socket_set import *
# from libraries.infrared import *
from libraries.buzzer import *

print "Initializing BattleBot Sequence (Servo)"

buzzer = buzzer();

# try a buzz, pitch/duration
buzzer.buzz(262, 1.0)



