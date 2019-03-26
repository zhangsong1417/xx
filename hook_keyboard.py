# coding:utf-8
# author:

import pyHook
import pythoncom


def onKeyBoardEvent(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')


def main():
    # 1.创建一个钩子管理器
    hm = pyHook.HookManager()
    # 2.监听到了目标事件，回调函数
    hm.KeyDown = onKeyBoardEvent()
    # 3.监听事件（按键事件）
    hm.Hookkeyboard()
    # 4.善后处理，消息顺利传递
    pythoncom.PumpMessages


if __name__=="__main__":
    main()
