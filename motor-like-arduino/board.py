from pyfirmata2 import Arduino
from .motor import Motor
from .exceptions import BoardConnectionError


class ArduinoBoard:

    def __init__(self, port):
        try:
            self.board = Arduino(port)
        except Exception as e:
            raise BoardConnectionError(str(e))

    def create_motor(self, direction1, direction2, pwm):
        return Motor(
            self.board,
            direction1,
            direction2,
            pwm
        )

    def close(self):
        self.board.exit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()