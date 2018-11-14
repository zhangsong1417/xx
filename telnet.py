# !/usr/bin/env python
# coding=utf-8
import sys
import telnetlib
import os
import time

enter = '\n'
filehead = "D:\\file\\"
filetail = ".txt"


def getfile(filename):
    f = open(filename, 'w+')
    while (1):
        ret = tn.read_until('>', 1)
        f.write(ret)
        if '>' in ret:
            break
        else:
            for i in range(10):
                tn.write(' ')
                time.sleep(0.1)
    f.close()


# check the file is existd or not

def get(string):
    tn.write(string + enter)
    filename = filehead + string.replace(' ', '-') + filetail
    getfile(filename)
    print()
    string + ' information is in ' + filename
    print()
    'Router#'


def login():
    #password = sys.argv[2]
    password = b"vorx"
    # get ordinary certificate
    tn.read_until(b"Password: ", 1)
    tn.write(password + enter)

    # want to get admin certificate
    tn.read_until(">", 1)
    tn.write('en' + enter)

    # get admin certificate
    tn.read_until("Password: ", 1)
    tn.write(password + enter)

    # enter route
    print
    tn.read_until("Router#", 1)


def options():
    showstring = ["show version",
                  "show arp",
                  "show run",
                  "show running-config",
                  "show startup-config",
                  "show ip interface brief",
                  "show ip route"]
    while 1:
        string = input()
        string = string.lower()
        if string == 'exit':
            tn.write('exit' + enter)
            print
            'exit success'
            break
        elif string in showstring:
            get(string)
        else:
            print
            'wrong input'
            print
            'please enter an order'


if __name__ == "__main__":
    #Host = sys.argv[1]
    Host = "192.168.20.10"
    tn = telnetlib.Telnet(Host)
    #login()
    options()