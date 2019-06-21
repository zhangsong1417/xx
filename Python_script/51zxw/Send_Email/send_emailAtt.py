import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.mime.multipart import MIMEMultipart  # 用于传送附件

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
# 构造附件内容
send_file = open(r"D:\xx\Python_script\51zxw\Send_Email\13.jpg", 'rb').read()
att = MIMEText(send_file, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="13.jpg"'
# 构建发送与接收信息
msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content, 'html', 'utf-8'))
msgRoot['subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = ','.join(receives)
msgRoot.attach(att)
# SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)
# 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录邮箱服务器用户名和密码
smtp.login(user, password)

print("Start send Email...")
smtp.sendmail(sender, receives, msgRoot.as_string())
smtp.quit()
print("Send Email End!")
