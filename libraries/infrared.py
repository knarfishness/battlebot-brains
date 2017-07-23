import serial

class infrared():
    def __init__(self):
        # Setup serial connection for communication with YS-IRTM module
        global ser
        ser = serial.Serial(
            port='/dev/ttyS0',
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )

    def shoot(self):
        # So the code you send will always start with A1, F1
        # because these are only used for the YS-IRTM to "start" sending the next bits.

        values = bytearray([0xA1, 0xF1, 0x42, 0x42, 0x42])
        # values = bytearray([0xA1, 0xF1, 0x02, 0x00, 0x02]) #uncomment for bot 2
        ser.write(values)

    def read(self):
        if (ser.inWaiting() > 0):
            return str(ser.read(ser.inWaiting()))
