# Changelog

All notable changes to motor-like-arduino will be documented in this file.

This project follows Semantic Versioning.

## [0.1.0] - Initial Release

### Added

#### Board Management

* `Board` class for connecting to Arduino boards running StandardFirmata
* Support for multiple motors on a single board connection
* Automatic board cleanup with `close()`
* Context manager support using `with`

#### Motor Management

* Create motors using `attach_motor()`
* Independent control of multiple motors
* Optional motor names for identification
* Motor registry available through `board.motors`

#### Motor Control

* `forward(speed)`
* `backward(speed)`
* `stop()`
* `brake()`
* `set_speed(speed)`

#### Speed Control

* Percentage-based speed values (`0-100`)
* Automatic speed validation
* Automatic PWM conversion

#### Motor State Tracking

* `motor.speed`
* `motor.direction`

Supported direction states:

* `forward`
* `backward`
* `stopped`
* `braked`

#### Board Utilities

* `stop_all()` for stopping every attached motor
* Optional TB6612FNG standby pin support
* `wake()` to enable the motor driver
* `sleep()` to place the motor driver into standby mode

#### Error Handling

* `MotorLikeArduinoError`
* `InvalidSpeedError`
* `BoardConnectionError`
* `StandbyNotConfiguredError`

#### Examples

Included example programs:

* `single_motor.py`
* `dual_motor.py`
* `tank_drive.py`
* `keyboard_control.py`

#### Compatibility

Tested design for motor drivers using:

* 2 direction pins
* 1 PWM pin

Including:

* TB6612FNG
* L293D
* L298N
* MX1508

#### Documentation

* Full README
* API reference
* Usage examples
* Installation guide

### Dependencies

* pyFirmata2

### Requirements

* Python 3.8+
* Arduino running StandardFirmata
