# motor-like-arduino

Arduino-style DC motor control for Python using Firmata.

Control motors with simple, beginner-friendly commands inspired by Arduino libraries.

```python
from motor_like_arduino import Board

board = Board("/dev/ttyUSB0")

left_motor = board.attach_motor(2, 4, 11)
right_motor = board.attach_motor(5, 3, 10)

left_motor.forward(50)
right_motor.forward(100)
```

---

## Features

* Simple Arduino-inspired API
* Control individual motors independently
* Speed control using percentages (0–100)
* Forward and backward movement
* Stop and brake functionality
* Shared board connection
* Context manager support
* Built on top of pyFirmata2
* Works with Arduino boards running StandardFirmata

---

## Installation

```bash
pip install motor-like-arduino
```

---

## Requirements

* Python 3.8+
* Arduino running StandardFirmata
* pyFirmata2 (installed automatically)

---

## Quick Start

```python
from motor_like_arduino import Board
import time

board = Board("/dev/ttyUSB0")

motor = board.attach_motor(
    direction1=2,
    direction2=4,
    pwm=11
)

motor.forward(100)
time.sleep(2)

motor.backward(50)
time.sleep(2)

motor.stop()

board.close()
```

---

## Dual Motor Example

```python
from motor_like_arduino import Board
import time

board = Board("/dev/ttyUSB0")

left_motor = board.attach_motor(
    direction1=2,
    direction2=4,
    pwm=11
)

right_motor = board.attach_motor(
    direction1=5,
    direction2=3,
    pwm=10
)

left_motor.forward(50)
right_motor.forward(100)

time.sleep(3)

left_motor.stop()
right_motor.stop()

board.close()
```

---

## API Reference

### Board

Create a connection to an Arduino running StandardFirmata.

```python
board = Board("/dev/ttyUSB0")
```

### Attach a Motor

```python
motor = board.attach_motor(
    direction1=2,
    direction2=4,
    pwm=11
)
```

### Motor Functions

#### Move Forward

```python
motor.forward(100)
```

#### Move Backward

```python
motor.backward(100)
```

#### Change Speed

```python
motor.set_speed(75)
```

#### Stop

Allows the motor to coast to a stop.

```python
motor.stop()
```

#### Brake

Actively brakes the motor for a faster stop.

```python
motor.brake()
```

---

## Motor Properties

### Current Speed

```python
print(motor.speed)
```

### Current Direction

```python
print(motor.direction)
```

Possible values:

```text
forward
backward
stopped
braked
```

---

## Context Manager Support

```python
from motor_like_arduino import Board

with Board("/dev/ttyUSB0") as board:

    motor = board.attach_motor(
        direction1=2,
        direction2=4,
        pwm=11
    )

    motor.forward(100)
```

The board connection is automatically closed when the block exits.

---

## Included Examples

The repository includes:

* single_motor.py
* dual_motor.py
* tank_drive.py
* keyboard_control.py

---

## License

MIT License

---

## Author

Vihaan Parlikar

GitHub: https://github.com/vihaanvp
