# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project follows Semantic Versioning.

---

## [0.1.0] - Initial Release

### Added

#### Board Management

* Board class for connecting to Arduino devices running StandardFirmata
* Shared board connection across multiple motors
* Automatic board cleanup
* Context manager support using `with`

#### Motor Management

* Individual motor objects
* `attach_motor()` helper method
* Independent control of multiple motors

#### Motor Functions

* `forward(speed)`
* `backward(speed)`
* `stop()`
* `brake()`
* `set_speed(speed)`

#### Speed Control

* Percentage-based speed values
* Supported range: 0–100
* Automatic PWM conversion

#### State Tracking

* `motor.speed`
* `motor.direction`

Supported directions:

* `forward`
* `backward`
* `stopped`
* `braked`

#### Error Handling

* Invalid speed validation
* Board connection exceptions

#### Examples

Added example programs:

* `single_motor.py`
* `dual_motor.py`
* `tank_drive.py`
* `keyboard_control.py`

#### Documentation

* Complete README
* API reference
* Installation instructions
* Usage examples

### Dependencies

* pyFirmata2

### Compatibility

* Python 3.8+
* Arduino boards running StandardFirmata
