#!/usr/bin/env python

# handle imports
from ps3 import *
from motor_control import *
from socket_set import *
from infrared import *
import time
import serial
import string

print "Initializing BattleBot Sequence (Servo)"

socket=socket_set()
socket.attempted_shot(123)
