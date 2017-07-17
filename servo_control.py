#####################################
# servo_control.py under RPI_FPVcar #
# --------------------------------- #
# Program written by Minsu Kim      #
# Last Update 17/07/17              #
# Author email: 521minsu@gmail.com  #
#####################################

import RPi.GPIO as GPIO

# Setting GPIO Pin layout as Board
GPIO.setmode(GPIO.BOARD)

# Pin def for servo motor
GPIO.setup(11,GPIO.OUT)


