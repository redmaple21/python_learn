import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 邮件设置
mail_host = 'smtp.thunisoft.com'
mail_user = 'wangfeng'
mail_passwrd = 'xxxxxx'

sender = 'wangfeng@thunisoft.com'
receivers = ['redmaple21@163.com']

message = MIMEText('Python 发送邮件demo 这是正文', 'plain', 'utf-8')
message['From'] = Header(sender, 'UTF-8')
message['To'] = Header('测试', 'UTF-8')
message['Subject'] = Header('测试邮件主题', 'UTF-8')

try:
    smtpClient = smtplib.SMTP()
    smtpClient.connect(mail_host, '25')
    smtpClient.login(mail_user, mail_passwrd)
    smtpClient.sendmail(sender, receivers, message.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print(e)
