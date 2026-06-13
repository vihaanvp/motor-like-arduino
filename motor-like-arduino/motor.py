from .exceptions import InvalidSpeedError


class Motor:

    def __init__(
        self,
        board,
        direction1,
        direction2,
        pwm
    ):
        self.direction1 = board.get_pin(
            f'd:{direction1}:o'
        )

        self.direction2 = board.get_pin(
            f'd:{direction2}:o'
        )

        self.pwm = board.get_pin(
            f'd:{pwm}:p'
        )

        self.speed = 0
        self.direction = "stopped"

    def _validate_speed(self, speed):
        if not 0 <= speed <= 100:
            raise InvalidSpeedError(
                "Speed must be between 0 and 100"
            )

    def _apply_speed(self, speed):
        self.pwm.write(speed / 100)

    def forward(self, speed=100):
        self._validate_speed(speed)

        self.direction1.write(1)
        self.direction2.write(0)

        self._apply_speed(speed)

        self.speed = speed
        self.direction = "forward"

    def backward(self, speed=100):
        self._validate_speed(speed)

        self.direction1.write(0)
        self.direction2.write(1)

        self._apply_speed(speed)

        self.speed = speed
        self.direction = "backward"

    def stop(self):
        self.direction1.write(0)
        self.direction2.write(0)

        self._apply_speed(0)

        self.speed = 0
        self.direction = "stopped"

    def brake(self):
        self.direction1.write(1)
        self.direction2.write(1)

        self._apply_speed(0)

        self.speed = 0
        self.direction = "braked"

    def set_speed(self, speed):
        self._validate_speed(speed)

        self._apply_speed(speed)
        self.speed = speed

    def reverse(self):
        if self.direction == "forward":
            self.backward(self.speed)

        elif self.direction == "backward":
            self.forward(self.speed)