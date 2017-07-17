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
<br>
*Warning: This program is still working in progress. <br>
*Warning: This program is tested on python 3.5 (May work with python2, but not yet tested, and possibly will not get tested) <br>
*Warning: This program is tested on Raspberry Pi 3 Model B (May work with other models but the GPIO pins might have to be changed) <br>
