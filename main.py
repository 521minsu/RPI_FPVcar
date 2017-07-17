####################################
# main.py under RPI_FPVcar         #
# -------------------------------- #
# Program written by Minsu Kim     #
# Last Update 17/07/17             #
# Author email: 521minsu@gmail.com #
####################################

from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application

from flasky import app

import motor_control

motor = motor_control


class MainHandler(RequestHandler):
    def get(self):
        self.write("This message comes from Tornado ^_^")

class TestClass(RequestHandler):
    def get(self):
        self.write("Test Usage from Tonado")


tr = WSGIContainer(app)


application = Application([
    (r"/tornado", MainHandler),
    (r"/test", TestClass),
    (r".*", FallbackHandler, dict(fallback=tr)),
])

if __name__ == "__main__":
    application.listen(8000)
    IOLoop.instance().start()
