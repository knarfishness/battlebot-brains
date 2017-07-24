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
    sys.stdout.write('sending')
    values = bytearray([0xA1, 0xF1, 0x41, 0x041, 0x41])
    # values = bytearray([0xA1, 0xF1, 0x42, 0x42, 0x42]) #uncomment for bot 2
    sys.stdout.write('test')
    ser.write(values)
    time.sleep(1)
