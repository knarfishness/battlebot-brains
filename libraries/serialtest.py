import serial
import time


def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
             return rv


port = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

while True: 
     rcv = readlineCR(port)
     port.write("I typed: " + repr(rcv))
     print(rcv)
