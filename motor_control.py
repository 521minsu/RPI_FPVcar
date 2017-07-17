#####################################
# motor_control.py under RPI_FPVcar #
# --------------------------------- #
# Program written by Minsu Kim      #
# Last Update 17/07/17              #
# Author email: 521minsu@gmail.com  #
#####################################

##################################################################
#  Enable |   A    |   B    | Result                             #
# -------------------------------------------------------------- #
#   LOW   |  HIGH  |  HIGH  | Not spinning - Enable is OFF       #
#   LOW   |  LOW   |  LOW   | Not spinning - Enable is OFF       #
#   HIGH  |  LOW   |  LOW   | Not spinning - Both Inputs are OFF #
#   HIGH  |  HIGH  |  LOW   | Turning Clockwise                  #
#   HIGH  |  LOW   |  HIGH  | Turning Anti-Clockwise             #
#   HIGH  |  HIGH  |  HIGH  | Not spinning - Both inputs are ON  #
##################################################################

import RPi.GPIO as GPIO

# Setting GPIO Pin layout as Board
GPIO.setmode(GPIO.BOARD)

# Pin def for motor1 - Left Motor
Motor1A = 16  # Pin A
Motor1B = 18  # Pin B
Motor1E = 22  # Enable Pin

# Pin def for motor2 - Right Motor
Motor2A = 23  # Pin A
Motor2B = 21  # Pin B
Motor2E = 19  # Enable Pin

# Setting Motor1 Pins as Output
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

# Setting Motor2 Pins as Output
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)


def motor1(direction):
    if direction == 1:  # Change the number 1 to 0 if the robot drives in the opposite way
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)
    elif direction == -1:
        GPIO.output(Motor1A, GPIO.LOW)
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)
    else:
        GPIO.output(Motor1E, GPIO.LOW)


def motor2(direction):
    if direction == 1:  # Change the number 1 to 0 if the robot drives in the opposite way
        GPIO.output(Motor2A, GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        GPIO.output(Motor2E, GPIO.HIGH)
    elif direction == -1:
        GPIO.output(Motor2A, GPIO.LOW)
        GPIO.output(Motor2B, GPIO.HIGH)
        GPIO.output(Motor2E, GPIO.HIGH)
    else:
        GPIO.output(Motor2E, GPIO.LOW)


def drive_one():
    motor1(0)   # Stops motor1
    motor2(1)   # Spins motor2 clockwise


def drive_two():
    motor1(1)   # Spins motor1 clockwise
    motor2(1)   # Spins motor2 clockwise


def drive_three():
    motor1(1)   # Spins motor1 clockwise
    motor2(0)   # Stops motor2


def drive_four():
    motor1(-1)  # Spins motor1 anti-clockwise
    motor2(1)   # Spins motor2 clockwise


def drive_five():
    motor1(0)   # Stops motor1
    motor2(0)   # Stops motor2


def drive_six():
    motor1(1)   # Spins motor1 clockwise
    motor2(-1)  # Spins motor2 anti-clockwise


def drive_seven():
    motor1(0)   # Stops motor1
    motor2(-1)  # Spins motor2 anti-clockwise


def drive_eight():
    motor1(-1)  # Spins motor1 anti-clockwise
    motor2(-1)  # Spins motor2 anti-clockwise


def drive_nine():
    motor1(-1)  # Spins motor1 anti-clockwise
    motor2(0)   # Stops motor2

