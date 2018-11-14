#!/usr/bin/python
import telnetlib
import time
import re


def do_telnet(Host, username, password, finish, commands):
    tn = telnetlib.Telnet(Host, port=23,timeout=10)
    tn.set_debuglevel(5)
    userinfo = tn.read_until(b'login:')
    tn.write(username + b"\r\n")
    pwdinfo = tn.read_until(b'Password:')
    tn.write(password + b"\r\n")
    loginfo = tn.read_until(finish)
    if isinstance(commands,list):
        for command in commands:
            tn.write('%s\n' % command)
    elif isinstance(commands,basestring):
        tn.write('%s\n' % commands)
    else:
        pass
    # wait 1 second for recv data
    time.sleep(1)
    info=tn.read_very_eager()
    return (userinfo + pwdinfo + loginfo + info)
    tn.close()
    # tn.write('exit\n')

def _test2():
    'test centos linux'
    host = b'192.168.20.10'
    log = do_telnet(host,b'vorx',b'vorx',b'>',b'ifconfig -a')
    print(log)


if __name__ == '__main__':
    _test2()