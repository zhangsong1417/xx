from selenium import webdriver
import os
import smtplib  # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header  # 定义邮件标题


def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)
    print(func_path)

    base_dir = os.path.dirname(func_path)
    print(base_dir)

    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')

    print(base_dir)
    base = base_dir.split('/Website')[0]
    print(base)

    filepath = base + '/Website/test_report/screenshot' + filename
    driver.get_screenshot_as_file(filepath)


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
    receives = ['zhangsong@vorx.com.cn', 'cyxzhangsong@163.com']
    # 发送邮件主题和内容
    subject = 'Web Seleniun自动化测试报告'
    # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
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
    # insert_img()
    driver = webdriver.Firefox()
    driver.get("http://www.sogou.com")
    insert_img(driver, 'Sougou.png')
    driver.quit()
