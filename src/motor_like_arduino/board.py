from pyfirmata2 import Arduino

from .motor import Motor
from .exceptions import (
    BoardConnectionError,
    StandbyNotConfiguredError
)


class Board:
    def __init__(self, port, stby=None):
        try:
            self._board = Arduino(port)
        except Exception as e:
            raise BoardConnectionError(str(e))

        self.motors = []

        if stby is not None:
            self._stby = self._board.get_pin(
                f"d:{stby}:o"
            )
            self._stby.write(1)
        else:
            self._stby = None

    def attach_motor(
        self,
        direction1,
        direction2,
        pwm,
        name=None
    ):
        motor = Motor(
            self._board,
            direction1,
            direction2,
            pwm,
            name
        )

        self.motors.append(motor)

        return motor

    def stop_all(self):
        for motor in self.motors:
            motor.stop()

    def wake(self):
        if self._stby is None:
            raise StandbyNotConfiguredError(
                "No STBY pin configured."
            )

        self._stby.write(1)

    def sleep(self):
        if self._stby is None:
            raise StandbyNotConfiguredError(
                "No STBY pin configured."
            )

        self._stby.write(0)

    def close(self):
        self.stop_all()

        if self._stby is not None:
            self._stby.write(0)

        self._board.exit()

    def __enter__(self):
        return self

    def __exit__(
        self,
        exc_type,
        exc_val,
        exc_tb
    ):
        self.close()