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
from libraries import ps3
from libraries import motor_control
from libraries import socket_set
from libraries import infrared
import time
import serial
import string

print ("Initializing BattleBot Sequence (Servo)")

# Delays for 15 seconds, enough for the PS3 controller
time.sleep(5)

# Create a PS3 controller object
p=ps3.ps3()

# Connect to the socket server
socket=socket_set.socket_set()
socket.register()

# Start the motor logic
motors=motor_control.motor_control()

# shoot values
values = bytearray([0xA1, 0xF1, 0x01, 0x00, 0x01])

ir = infrared.infrared()

penalty_time = 5

# end init sequence
#print "Serial is open: " + str(ir.isOpen())
print ("BattleBot Sequence Complete. BattleBot is GO!")

# Main Loop
while True:
    # let's read the IR transmitter to see if we've been hit first
    if(ir.read() == 'AAA'):
        print("I've been hit!")
        socket_set.hit()
        time.sleep(penalty_time)

    # Reads in the values from the PS3 controller
    p.update()

    # determine based off of L1 or R1 if we should be firing during this loop
    if( p.r1 or p.l1 ):
        ir.shoot()
        socket.fire()
        print ("Shots Fired!")

    # process joystick input and produce movement in the absence of hit events
    motors.handle_joystick_input(p)

    # for stability
    time.sleep(0.1)
