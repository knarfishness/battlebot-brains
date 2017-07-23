from Adafruit_MotorHAT import Adafruit_MotorHAT
import time

class motor_control:
    def __init__(self):
        # Initialise the PWM device using the default address
        mh = Adafruit_MotorHAT(0x60)

        # Reverse these values to switch motor sides
        left_id = 2
        right_id = 1
        global backward
        global forward
        global left
        global right
        backward = Adafruit_MotorHAT.BACKWARD
        forward = Adafruit_MotorHAT.FORWARD
        left = mh.getMotor(left_id)
        right = mh.getMotor(right_id)

        # Start with motors turned off
        left.run(Adafruit_MotorHAT.RELEASE)
        right.run(Adafruit_MotorHAT.RELEASE)

    def right_forward(self, right_stick):
        rightSpeed = abs((right_stick-90)*2.8)
        right.setSpeed(int(rightSpeed))
        right.run(forward)

    def right_reverse(self, right_stick):
        rightSpeed = abs((right_stick-90)*2.8)
        right.setSpeed(int(rightSpeed))
        right.run(backward)

    def right_release(self):
        right.run(Adafruit_MotorHAT.RELEASE)

    def left_forward(self, left_stick):
        leftSpeed = abs((left_stick-90)*2.8)
        left.setSpeed(int(leftSpeed))
        left.run(forward)

    def left_reverse(self, left_stick):
        leftSpeed = abs((left_stick-90)*2.8)
        left.setSpeed(int(leftSpeed))
        left.run(backward)

    def left_release(self):
        left.run(Adafruit_MotorHAT.RELEASE)

    def penalty_on_hit(self):
        self.left_release()
        self.right_release()
        time.sleep(5)

    def handle_joystick_input(self, p):
        # value will be 90 at neutral, 0 at full throttle and 179 at full down
        left_stick = (p.a_joystick_left_y+1)*90
        right_stick = (p.a_joystick_right_y+1)*90

        # speed control logic, left
        if left_stick > 90:
            self.left_forward(left_stick)
        elif left_stick < 90:
            self.left_reverse(left_stick)
        else:
            self.left_release()

        # speed control logic, right
        if right_stick > 90:
            self.right_forward(right_stick)
        elif right_stick < 90:
            self.right_reverse(right_stick)
        else:
            self.right_release()


