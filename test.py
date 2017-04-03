#!/usr/bin/env python
########################################################################                                               
# This example controls a Raspberry Pi Motor Hat using a PS3 Dual-shock 3 controller
#                                
# History
# ------------------------------------------------
# Author        Date            Comments
# Frank Avery   2 Feb 2017      Initial Authoring
# Frank Avery   1 Apr 2017      Initial serial and socket work
# Frank Avery   2 Apr 2017      Code Organization
#

########################################################################

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
