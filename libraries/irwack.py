import serial
import time
import sys


ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)


while True:
    values = bytearray([0xA1, 0xF1, 0x01, 0x00, 0x01])
    # values = bytearray([0xA1, 0xF1, 0x02, 0x00, 0x02]) #uncomment for bot 2
    ser.write(values)
    time.sleep(3)
