import os
from configparser import ConfigParser

# Config Class
class Config(object):

    # initial func
    def __init__(self, BASE_PATH):
        # initial global val
        self.BASE_PATH = BASE_PATH
        self.GLOBAL_FILENAME = 'global.conf'
        self.CONF_PATH = '{}/conf'.format(self.BASE_PATH)
        self.CONF_FILE = '{}/{}'.format(self.CONF_PATH, self.GLOBAL_FILENAME)

        # ERROR CODE
        self.SUCCESS_EXIT     = 0
        self.ERROR_PROC_EXIST = 1

        # initial configObj
        configParserObj = ConfigParser()
        configParserObj.read(self.CONF_FILE)

        # initial config val
        self.MAIL_ENABLE = configParserObj.get('MAIL', 'ENABLE').upper()
        if self.MAIL_ENABLE == 'TRUE':
            self.MAIL_ENABLE = True

        else:
            self.MAIL_ENABLE = False

        self.MAIL_TO = configParserObj.get('MAIL', 'TO')
        self.MAIL_USER = configParserObj.get('MAIL', 'USER')
        self.MAIL_HOST = configParserObj.get('MAIL', 'HOST')
        self.MAIL_PORT = configParserObj.get('MAIL', 'PORT')
        self.MAIL_PASSWORD = configParserObj.get('MAIL', 'PASSWORD')

        self.LOG_PATH = '{}/{}'.format(self.BASE_PATH, configParserObj.get('LOG', 'LOG_PATH'))
        self.LOG_FILE = '{}/{}'.format(self.LOG_PATH, configParserObj.get('LOG', 'LOG_FILE'))
        self.LOG_LEVEL = configParserObj.get('LOG', 'LOG_LEVEL').upper()
        self.LOG_MAX_SIZE = int(configParserObj.get('LOG', 'LOG_MAX_SIZE')) * 1024 * 1024
        self.LOG_BACKUP_COUNT = int(configParserObj.get('LOG', 'LOG_BACKUP_COUNT'))

        # initial base dir
        self.dir_init(self.LOG_PATH)

    # directory initial function
    def dir_init(self, dir):
        if not os.path.exists(dir):
            try:
                os.mkdir(dir)

            except Except as e:
                sys.stderr.write('[Error][%s]' % (e))
                sys.stderr.flush()

        return(True)
