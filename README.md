# motor-like-arduino

Arduino-style DC motor control for Python.

Control motors connected to an Arduino running StandardFirmata using simple, intuitive commands inspired by the Arduino ecosystem.

```python
from motor_like_arduino import Board

board = Board("/dev/ttyUSB0")

motor = board.attach_motor(2, 4, 11)

motor.forward(100)
```

---

## Why motor-like-arduino?

Most Python motor libraries expose low-level motor driver details.

motor-like-arduino focuses on simplicity:

```python
motor.forward(100)
motor.backward(50)
motor.stop()
motor.brake()
```

No PWM calculations.

No complicated setup.

Just simple motor control.

---

## Installation

```bash
pip install motor-like-arduino
```

---

## Quick Start

```python
from motor_like_arduino import Board
import time

board = Board("/dev/ttyUSB0")

motor = board.attach_motor(
    2,  # Direction Pin 1
    4,  # Direction Pin 2
    11  # PWM Pin
)

motor.forward(100)

time.sleep(2)

motor.stop()

board.close()
```

---

## Multiple Motors

```python
from motor_like_arduino import Board

board = Board("/dev/ttyUSB0")

left_motor = board.attach_motor(
    2,
    4,
    11
)

right_motor = board.attach_motor(
    5,
    3,
    10
)

left_motor.forward(50)
right_motor.forward(100)
```

---

## Features

* Simple Arduino-inspired API
* Percentage-based speed control (0-100)
* Forward and backward movement
* Stop and brake support
* Multiple motors per board
* Optional TB6612FNG standby support
* Automatic speed validation
* Safe board shutdown
* Context manager support
* Custom exceptions
* Built on top of pyFirmata2

---

## Supported Motor Drivers

Any motor driver that uses:

* 2 direction pins
* 1 PWM pin

Including:

* TB6612FNG
* L293D
* L298N
* MX1508

---

## Optional TB6612FNG Standby Support

```python
board = Board(
    "/dev/ttyUSB0",
    stby=6
)
```

```python
board.sleep()
board.wake()
```

---

## Included Examples

The repository includes ready-to-run examples:

* Single Motor Control
* Dual Motor Control
* Tank Drive
* Keyboard Control

---

## Documentation

Complete documentation, API reference, guides, and examples are available in the project wiki.

---

## Requirements

* Python 3.8+
* Arduino running StandardFirmata

---

## Author

Vihaan Parlikar

---