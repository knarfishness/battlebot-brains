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
from socketsetup import *
from infrared import *
import time
import serial
import string

print "Initializing BattleBot Sequence (Servo)"

# Delays for 15 seconds, enough for the PS3 controller
time.sleep(15) 

# Create a PS3 controller object
p=ps3()

# Connect to the socket server
socket=socket_set()

# Start the motor logic
motors=motor_control()()

# Initialize the Infrared Combat Unit
ir=infrared()

# end init sequence
print "Serial is open: " + str(ser.isOpen())
print "BattleBot Sequence Complete. BattleBot is GO!"

# Main Loop
while True:
    # let's read the IR transmitter to see if we've been hit first
    x = ser.readline()

    # hit events will be an ID
    if(x !== '') {
        botID = x;
        # SOCKET: send an event to the sever indicating you've been hit
        socket_set.i_have_been_shot(botID)
    }

    # Reads in the values from the PS3 controller
    p.update()

    # determine based off of L1 or R1 if we should be firing during this loop
    if( p.r1 || p.l1 ) {
        ir.shoot()
    }

    # process joystick input and produce movement in the absence of hit events
    motors.handle_joystick_input()

    # for stability
    time.sleep(.01)
