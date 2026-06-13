from .exceptions import InvalidSpeedError


class Motor:
    def __init__(
        self,
        board,
        direction1,
        direction2,
        pwm,
        name=None
    ):
        self._direction1 = board.get_pin(
            f"d:{direction1}:o"
        )

        self._direction2 = board.get_pin(
            f"d:{direction2}:o"
        )

        self._pwm = board.get_pin(
            f"d:{pwm}:p"
        )

        self.name = name

        self._speed = 0
        self._direction = "stopped"

    def __repr__(self):
        return (
            f"Motor("
            f"direction='{self._direction}', "
            f"speed={self._speed})"
        )

    def _validate_speed(self, speed):
        if not isinstance(speed, (int, float)):
            raise InvalidSpeedError(
                "Speed must be a number."
            )

        if not 0 <= speed <= 100:
            raise InvalidSpeedError(
                "Speed must be between 0 and 100."
            )

    def _apply_speed(self, speed):
        self._pwm.write(speed / 100)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self.set_speed(speed)

    @property
    def direction(self):
        return self._direction

    def forward(self, speed=100):
        self._validate_speed(speed)

        self._direction1.write(1)
        self._direction2.write(0)

        self._apply_speed(speed)

        self._speed = speed
        self._direction = "forward"

    def backward(self, speed=100):
        self._validate_speed(speed)

        self._direction1.write(0)
        self._direction2.write(1)

        self._apply_speed(speed)

        self._speed = speed
        self._direction = "backward"

    def stop(self):
        self._direction1.write(0)
        self._direction2.write(0)

        self._apply_speed(0)

        self._speed = 0
        self._direction = "stopped"

    def brake(self):
        self._direction1.write(1)
        self._direction2.write(1)

        self._apply_speed(0)

        self._speed = 0
        self._direction = "braked"

    def set_speed(self, speed):
        self._validate_speed(speed)

        self._apply_speed(speed)
        self._speed = speed