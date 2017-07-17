from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_world():
  return 'This comes from Flask ^_^'

@app.route('/servo/<angle>')
def control_servo(angle):
    return 'Angle: {}'.format(angle)