# RPI_FPVcar
<br>
This program allows Raspberry Pi to open up a webserver on port no. 8000 with python, and allows android phones to control the robot by accessing specific urls. <br>
<br>
In order to read the latest url that the client has issued, and execute functions accordingly, this program uses tornado to open up the webserver, and flask to read variables on the url. <br>
<br>
Please install the latest tornado, and flask modules from their official websites listed below and execute this program. <br>
<br>
Tornado: <br>
http://www.tornadoweb.org/en/stable/ <br>
<br>
Flask: <br>
http://flask.pocoo.org/ <br>
<br>
# To run this program <br>
1. Clone or download and unzip this repo into your Raspberry Pi  <br>
2. cd into the directory <br>
3. issue following command on ssh or terminal: $ sudo python3 main.py (You may try python, but this program is tested on 3.5) <br>
<br>
*Warning: DON'T FORGET TO INSTALL MODULES IN PYTHON3 <br>
*Warning: This program is still working in progress. (Guessing this project will finish in this year at the most) <br>
*Warning: This program is tested on python 3.5 (May work with python2, but not yet tested, and possibly will not get tested) <br>
*Warning: This program is tested on Raspberry Pi 3 Model B (May work with other models but the GPIO pins might have to be changed) <br>
