# -*- coding: utf-8 -*-

import telnetlib
import time

def telnetip():
    # 连接Telnet服务器
    tn = telnetlib.Telnet(ip, port=23, timeout=50)
    # 输入登录用户名
    tn.read_until(b'Username:')
    tn.write(username + b'\n')

    # 输入登录密码
    tn.read_until('Password:')
    tn.write(password + b'\r\n')
    time.sleep(1)
    tn.write(b'system' + b'\n')  # 输入命令
    tn.write(b'configuration' + b'\n')
    tn.write(b'****' + b'\n')
    tn.write(b'****' + b'\n')
    time.sleep(50)
    result1 = tn.read_very_eager()  # 获得结果
    print(result1)
    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()  # tn.write('exit\n')

if __name__ == '__main__':
    # 配置选项
    ip = '192.168.20.10'  # Telnet交换机IP
    username = b'vorx'  # 登录用户名
    password = b'vorx'  # 登录密码
    #telnetip(ip)