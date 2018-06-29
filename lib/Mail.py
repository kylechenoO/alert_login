import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# Mail class
class Mail(object):
    
    def __init__(self, configObj, logger, sysuser):
        # initial global val
        self.conf = configObj
        self.logger = logger
        self.sysuser = sysuser

        self.MAIL_ENABLE = configObj.MAIL_ENABLE
        self.MAIL_TO = configObj.MAIL_TO
        self.MAIL_USER = configObj.MAIL_USER
        self.MAIL_HOST = configObj.MAIL_HOST
        self.MAIL_PORT = configObj.MAIL_PORT
        self.MAIL_PASSWORD = configObj.MAIL_PASSWORD
        self.loginTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    # send mail
    def send(self):

        if not self.MAIL_ENABLE:
            self.logger.info('Mail Module Disabled')
            return(False)

        subject = '[{}][{}]Login Message'.format(self.loginTime, self.sysuser)
        message = 'LoginTime:{}\nUser:{}\nType:Login Message'.format(self.loginTime, self.sysuser)
        message = MIMEText(message, 'plain', 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        message['From'] = Header(self.MAIL_USER, 'utf-8')
        message['To'] = Header(self.MAIL_TO, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(self.MAIL_HOST, self.MAIL_PORT)
            smtpObj.login(self.MAIL_USER,self.MAIL_PASSWORD)  
            smtpObj.sendmail(self.MAIL_USER, self.MAIL_TO, message.as_string())
            self.logger.info('Send Mail Succeed')

        except smtplib.SMTPException:
            self.logger.info('Send Mail Failed')
            return(False)

        return(True)
