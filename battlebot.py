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
# Frank Avery   23 Jul 2017     Added sounds and better logic
#

########################################################################

# handle imports
from libraries import ps3
from libraries import motor_control
from libraries import socket_set
from libraries import infrared
from libraries import buzzer
import time
import serial
import string
import pygame
import os
import sys

print ("Initializing BattleBot Startup Sequence...")

# Attempt to connect to a PS3 controller
p = None
while p is None:
    try:
        print ("Looking for a controller...")
        p = ps3.ps3()
    except:
        print("No controller found, trying again in 2 seconds.")
        p = None
        time.sleep(2)
        os.execl(sys.executable, sys.executable, *sys.argv)

# Start the motor logic
motors=motor_control.motor_control()

# Initialize the IR send/receive module
ir = infrared.infrared()

# Create a buzzer object to make sounds with
buzzer = buzzer.buzzer()

# Set a int for penalty when hit
penalty_time = 5
reload_time = 1

socket = None

print ("BattleBot Sequence Complete. BattleBot is GO!")

# Main Loop
while True:
    data = str(ir.read())
    # let's read the IR transmitter to see if we've been hit first
    if "BBB" in data:
        print("I've been hit!")
        #socket_set.hit()
        buzzer.buzz(128, 1.0)
        motors.penalty_on_hit()
        clear = ir.read()
        if( socket ):
            socket.hit()

    # Reads in the values from the PS3 controller
    try:
        p.update()
    except:
        print("Controller lost!")
        

    # attempt to bind to the socket server if the start button is pressed
    if ( p.start ):
        if socket is None:
            # Connect to the socket server
            buzzer.buzz(288, 0.1)
            try:
                socket=socket_set.socket_set()
            except:
                break
            socket.register()
        else:
            # we're already connected
            print ("Already connected to server")
            buzzer.buzz(102, 0.1)


    # determine based off of L1 or R1 if we should be firing during this loop
    if( p.r1 ):
        print ("Firing Main Cannon")
        buzzer.buzz(220, 0.1)
        ir.shoot()
        if( socket ):
            socket.fire()

    if( p.l1 ):
        print ("Grenade Fired!")
        buzzer.buzz(100, 0.2)

    # process joystick input and produce movement in the absence of hit events
    motors.handle_joystick_input(p)

    # for stability
    time.sleep(0.1)
