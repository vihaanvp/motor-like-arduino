from motor_like_arduino import ArduinoBoard
import time

with ArduinoBoard("/dev/ttyUSB0") as board:

    motor = board.create_motor(
        direction1=2,
        direction2=4,
        pwm=11
    )

    motor.forward(100)

    time.sleep(2)

    motor.stop()