from termcolor import colored
from datetime import datetime

class Logger(object):

    def __init__(self):
        self.ids_and_colors = {}
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'] * 100

    def info(self, id, message):
        color = self._get_color(id)
        attrs = []
        print str(datetime.now()) + " " + "[%s] %s" % (id, message)

    def _get_color(self, id):
        if id not in self.ids_and_colors:
            self.ids_and_colors[id] = self.colors.pop()

        return self.ids_and_colors[id]

