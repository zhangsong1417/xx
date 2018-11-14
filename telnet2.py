# -*- coding: utf-8 -*-
import sys
import telnetlib
import time

'''Telnet远程登录：Windows客户端连接Linux服务器'''

# 配置选项
Host = '192.168.20.10'  # Telnet服务器IP
username = b'vorx'      # 登录用户名
password = b'vorx'      # 登录密码
command = b"port configuration"
finish = b'>'       # 命令提示符（标识着上一条命令已执行完毕）

# 连接Telnet服务器
tn = telnetlib.Telnet(Host)
tn.set_debuglevel(2)
print("正在加载，请稍后---")
time.sleep(5)
# 输入登录用户名
tn.read_until(b'Username:')
tn.write(username + b"\r\n")

# 输入登录密码
tn.read_until(b'Password:')
tn.write(password + b'\r\n')

# 登录完毕后，执行ls命令
tn.read_until(finish)
print("登录成功，执行port configuration命令")

tn.write(command + b'\r\n')
print("开始返回数据")
# 命令执行完毕后，终止Telnet连接（或输入exit退出）

s = tn.get_socket()
print(s)

tn.read_until(finish)
result = tn.read_all()
#tn.read_very_eager()
time.sleep(10)
print(result)

#print(result.decode('gbk'))
'''log_file = open('D:\\xx\\1.txt',"w+")
log_file.write(result)
log_file.flush()
log_file.close()'''
print("....获取结束....")
tn.close()
tn.write(b'exit\n')

