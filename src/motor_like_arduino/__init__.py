from .board import Board
from .motor import Motor

from .exceptions import (
    MotorLikeArduinoError,
    InvalidSpeedError,
    BoardConnectionError,
    StandbyNotConfiguredError
)

from .version import __version__

__all__ = [
    "Board",
    "Motor",
    "MotorLikeArduinoError",
    "InvalidSpeedError",
    "BoardConnectionError",
    "StandbyNotConfiguredError",
    "__version__"
]