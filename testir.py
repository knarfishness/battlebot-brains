import serial
serialData = serial.Serial("/dev/ttyAMA0",115200);
try:
    print "hey"
