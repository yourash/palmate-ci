import logging
import colorlog
import sys

class Logger:
    def __init__(self, fname, level='INFO'):
        if fname:
        	for arg in sys.argv[1:]:
        		try:
        			self.fname = open(fname, 'w')
        		except IOError:
        			print('cannot open', arg)
        			self.fname = None
        		else:
        			self.fname = None

        self.logger = logging.getLogger()
        self.handler = colorlog.StreamHandler()
        self.handler.setFormatter(colorlog.ColoredFormatter(
                '%(asctime)s %(log_color)s%(levelname)s:%(name)s:%(message)s%(reset)s',
                log_colors={
                    'INFO': 'green',
                    'WARNING': 'yellow',
                    'ERROR': 'red'
                    }))
        self.logger.addHandler(self.handler)
        self.setLevel(level)

    def setLevel(self, level):
        if level == 'INFO':
            self.logger.setLevel(logging.INFO)
        elif level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif level == 'ERROR':
            self.logger.setLevel(logging.ERROR)

    def info(self, message):
        self.logger.info(message)
        if self.fname is not None:
            self.fname.println('[INFO] %s' % message)

    def warn(self, message):
        self.logger.warning(message)
        if self.fname is not None:
            self.fname.println('[WARNING] %s' % message)

    def error(self, message):
        self.logger.error(message)
        if self.fname is not None:
            self.fname.println('[ERROR] %s' % message)

