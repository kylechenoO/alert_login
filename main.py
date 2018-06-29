import os
import sys
from lib.Log import Log
from lib.Mail import Mail
from lib.Config import Config

if __name__ == '__main__':

    # initial val
    BASE_PATH = os.path.abspath(os.path.dirname(__file__))

    # read config
    configObj = Config(BASE_PATH)
    logObj = Log(configObj)
    logger = logObj.get_logger()

    #debug print
    logger.debug('MAIL_ENABLE {}'.format(configObj.MAIL_ENABLE))
    logger.debug('MAIL_TO {}'.format(configObj.MAIL_TO))
    logger.debug('MAIL_USER {}'.format(configObj.MAIL_USER))
    logger.debug('MAIL_HOST {}'.format(configObj.MAIL_HOST))
    logger.debug('MAIL_PORT {}'.format(configObj.MAIL_PORT))
    logger.debug('LOG_PATH {}'.format(configObj.LOG_PATH))
    logger.debug('LOG_FILE {}'.format(configObj.LOG_FILE))
    logger.debug('LOG_MAX_SIZE {}'.format(configObj.LOG_MAX_SIZE))
    logger.debug('LOG_BACKUP_COUNT {}'.format(configObj.LOG_BACKUP_COUNT))

    # argc check
    if len(sys.argv) != 2:
        logger.error('Need User')
        sys.exit(configObj.ERROR_PROC_EXIST)

    sysuser = sys.argv[1]

    # initial ddnsObj
    mailObj = Mail(configObj, logger, sysuser)
    mailObj.send()

    # success exit
    sys.exit(configObj.SUCCESS_EXIT)
