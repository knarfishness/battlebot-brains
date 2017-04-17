from Adafruit_PWM_Servo_Driver import PWM
import time

class motor_control:
    def __init__(self):
        # Initialise the PWM device using the default address
        pwm = PWM(0x60)

        # Reverse these values to switch motor sides
        left_id = 2
        right_id = 1
        left = mh.getMotor(left_id)
        right = mh.getMotor(right_id)

        # Start with motors turned off
        left.run(Adafruit_MotorHAT.RELEASE)
        right.run(Adafruit_MotorHAT.RELEASE)

    def right_forward():
        rightSpeed = abs((right_stick-90)*2.8)
        right.setSpeed(int(rightSpeed))
        right.run(Adafruit_MotorHAT.FORWARD)

    def right_reverse():
        rightSpeed = abs((right_stick-90)*2.8)
        right.setSpeed(int(rightSpeed))
        right.run(Adafruit_MotorHAT.BACKWARD)

    def right_release():
        right.run(Adafruit_MotorHAT.RELEASE)

    def left_forward(left_stick):
        leftSpeed = abs((left_stick-90)*2.8)
        left.setSpeed(int(leftSpeed))
        left.run(Adafruit_MotorHAT.FORWARD)

    def left_reverse():
        leftSpeed = abs((left_stick-90)*2.8)
        left.setSpeed(int(leftSpeed))
        left.run(Adafruit_MotorHAT.BACKWARD)

    def left_release():
        left.run(Adafruit_MotorHAT.RELEASE)

    def penalty_on_hit():
        left_release()
        right_release()
        time.sleep(5)

    def handle_joystick_input():
        # value will be 90 at neutral, 0 at full throttle and 179 at full down
        left_stick = (p.a_joystick_left_y+1)*90
        right_stick = (p.a_joystick_right_y+1)*90

        # speed control logic, left
        if left_stick > 90:
            motors.left_forward(left_stick)
        elif left_stick < 90:
            motors.left_reverse(left_stick)
        else:
            motors.left_release()

        # speed control logic, right
        if right_stick > 90:
            motors.right_forward(right_stick)
        elif right_stick < 90:
            motors.right_reverse(right_stick)
        else:
            motors.right_release()

