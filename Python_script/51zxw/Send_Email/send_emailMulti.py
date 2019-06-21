import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题
# 发送邮件服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户名密码
user = 'shuiling21@163.com'
password = 'jiajia130182'
# 发送和接收邮箱
sender = 'shuiling21@163.com'
receives = ['zhangsong@vorx.com.cn', 'cyxzhangsong@163.com']
# 发送邮件主题和内容
subject = 'Web Seleniun自动化测试报告'
content = '<html><h1 style="color:red">自学成才!</h1></html>'
# HTML邮件正文
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'shuiling21@163.com'
msg['To'] = ','.join(receives)
# SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)
# 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录邮箱服务器用户名和密码
smtp.login(user, password)

print("Start send Email...")
smtp.sendmail(sender, receives, msg.as_string())
smtp.quit()
print("Send Email End!")
