#!/usr/bin/env python

# handle imports
import time
import serial
import string

# handle libraries
from libraries.ps3 import *
from libraries.motor_control import *
from libraries.socket_set import *
from libraries.infrared import *

print "Initializing BattleBot Sequence (Servo)"

bot1=socket_set()
bot2=socket_set()

bot1.fire(123)
bot1.fire(123)
bot2.hit(123)
bot1.fire(123)
bot1.fire(123)
bot2.hit(123)
bot1.fire(123)
bot1.fire(123)
bot2.hit(123)
bot1.fire(123)
bot1.fire(123)
bot2.hit(123)
bot1.fire(123)
bot1.fire(123)
bot2.hit(123)
bot1.fire(123)
bot1.fire(123)
bot2.hit(123)

