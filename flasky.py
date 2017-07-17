####################################
# flasky.py under RPI_FPVcar       #
# -------------------------------- #
# Program written by Minsu Kim     #
# Last Update 17/07/17             #
# Author email: 521minsu@gmail.com #
####################################

from flask import Flask
import motor_control

motor = motor_control
app = Flask(__name__)


@app.route('/motor/<joystick_angle>')
def motor_control_call(joystick_angle):
    motor.control(joystick_angle)
    print('Received Motor dir: {}'.format(joystick_angle))
    return 'Received Motor dir: {}'.format(joystick_angle)
