from motor_like_arduino import ArduinoBoard
import time

with ArduinoBoard("/dev/ttyUSB0") as board:

    left = board.create_motor(2, 4, 11)
    right = board.create_motor(5, 3, 10)

    left.forward(50)
    right.forward(100)

    time.sleep(3)

    left.stop()
    right.stop()