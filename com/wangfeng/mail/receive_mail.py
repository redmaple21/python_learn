import poplib
from email.parser import Parser

user = 'wangfeng@thunisoft.com'
password = 'xxxxxx'
pop3_address = 'pop3.thunisoft.com'

server = poplib.POP3_SSL(pop3_address)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(user)
server.pass_(password)

print("信息数量：%s 占用空间 %s" % server.stat())
print(server.list())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, ocetes = server.retr(1)
print(lines)
msg_content = b"\r\n".join(lines).decode("utf-8")
# 解析邮件
msg = Parser().parsestr(msg_content)
print(msg)
server.quit()
