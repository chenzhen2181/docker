from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib
#from gupiao.items import GupiaoItem

ifsendemail =False
def send_email(gp_name='a',gp_price='0.0'):
        msg = MIMEText(gp_name + gp_price, 'plain', 'utf-8')
        msg['Subject'] = Header(gp_name + gp_price, 'utf-8')
        send_addr = '120332986@qq.com'
        to_addr = '19955206682@189.cn'
        password = 'wcdyertkfolsbhbg'
        smtp_server = 'smtp.qq.com'
        server = smtplib.SMTP(smtp_server, 587)
        server.starttls()
        server.set_debuglevel(1)
        server.login(send_addr, password)
        server.sendmail(send_addr, [to_addr], msg.as_string())
        server.quit()
        global ifsendemail
        ifsendemail = True

