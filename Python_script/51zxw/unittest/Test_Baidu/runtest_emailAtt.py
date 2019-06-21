import unittest
from BSTestRunner import BSTestRunner
import time
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.mime.multipart import MIMEMultipart  # 用于传送附件
import os


def send_mail(latest_report):
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    # 发送邮件服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名密码
    user = 'shuiling21@163.com'
    password = 'jiajia130182'
    # 发送和接收邮箱
    sender = 'shuiling21@163.com'
    receives = ['zhangsong1417@foxmail.com', 'cyxzhangsong@163.com']
    # 发送邮件主题和内容
    subject = 'Web Seleniun自动化测试报告'
    # 构造附件内容
    att = MIMEText(mail_content, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename=%s' % report_name
    # 构建发送与接收信息
    msg = MIMEMultipart()
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(receives)
    msg.attach(att)
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


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("the latest report is" + lists[-1])
    # 输出最新报告的路径
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file


if __name__ == '__main__':
    # 存放报告文件夹
    report_dir = './test_report'
    # 定义测试用例路径
    test_dir = './test_case'
    discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H.%M.%S")
    # 报告文件完整路径
    report_name = report_dir + '/' + now + ' result.html'
    # 打开文件在报告文件写入测试结果
    with open(report_name, 'wb')as f:
        runner = BSTestRunner(stream=f, title='Test Report', description="Test case Report")
        runner.run(discovery)
    f.close()
    # 获取最新测试报告
    latest_report = latest_report(report_dir)
    # 发送邮件报告
    send_mail(latest_report)
