import smtplib
from email.mime.text import MIMEText
from email.header import Header
import logging
logging.basicConfig(filename='emailme-log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class EmailMe():

    def __init__(self, user_adress, user_name="", passwd_authorization="", mail_host="smtp.163.com", mail_port=465, SSL=True):
        r"""

        Argument:
        user_adress: string befor `@` or name shown in the mail page
        
        """
        self.adress = user_adress
        if user_name == "":
            self.user_name = user_adress
        else:
            self.user_name = user_name
        self.passwd = passwd_authorization
        self.host = mail_host
        self.port = mail_port
        if not SSL:
            self.port = 25
    
    def send_email(self, receiver_adress=[], receiver_name="", message="", subject=""):
        if receiver_adress == []:
            receiver_adress = self.adress
        if receiver_name == "":
            receiver_name = receiver_adress
        if message == "":
            return

        message = MIMEText(message, 'plain', 'utf-8')
        message['From'] = Header(self.adress, 'utf-8')
        message['To'] =  Header(receiver_adress[0], 'utf-8')

        if subject == "":
            subject = "确认作业"
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(self.host, self.port) 
            smtpObj.login(self.adress, self.passwd)
            # smtpObj.connect(self.host, self.port)
            # smtpObj.login(self.adress, self.passwd)  
            smtpObj.sendmail(self.adress, receiver_adress, message.as_string())
            smtpObj.close()
            logging.info("send email ok")
        except Exception as e:
            logging.warning("send email erro:\n email:{}\n exception: {}".format(message.as_string(), e))


if __name__ == "__main__":
    user_adress = "xxx@163.com"
    user_name = "sraps"
    authorization = "XXXX"
    passwd = authorization
    mail_host = "smtp.163.com"
    mail_port = 465

    amail = EmailMe(user_adress, user_name, passwd, mail_host, mail_port)

    msg = "程序运行完毕"

    receiver_adress = "xxx@qq.com"
    receiver_adress = [user_adress]
    receiver_name = "sraps"
    subject = "作业运行情况"

    amail.send_email(receiver_adress, receiver_name, msg, subject)



