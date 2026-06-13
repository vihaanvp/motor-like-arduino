class MotorLikeArduinoError(Exception):
    pass


class InvalidSpeedError(MotorLikeArduinoError):
    pass


class BoardConnectionError(MotorLikeArduinoError):
    pass