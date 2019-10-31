# -*- coding: utf-8 -*- 
import time

import win32gui
import win32con
import win32api

from pynput import keyboard
import pynput.mouse
import pyperclip #剪切板

from baidu_translate import translateToChinese

# mystr = "你好啊,世界！"

def sendMessageToWindow(mystr):
    kids = []
    count = 0
    def all_ok(hwnd, param):
        # global count
        # print("%x "%hwnd, count, end='。');count+=1
        kids.append(hwnd)
        return True

    parent_hwnd = win32gui.FindWindow(None,u"朗读女 8.992")
    #print("parent:%x"%parent_hwnd)
    win32gui.EnumChildWindows(parent_hwnd, all_ok, None)
    my_hwnd = kids[224] #第x个是我要找的窗口
    #print("my_hwnd:%x "%my_hwnd)

    win32api.SendMessage(my_hwnd, win32con.WM_SETTEXT, None, mystr)
    # print("send message,finish!")
    print("译文：",mystr)

kbd = keyboard.Controller()
mouse = pynput.mouse.Controller()

def _control_C():
    #control + C 复制
    kbd.press(keyboard.Key.ctrl_l)
    kbd.press('c')
    time.sleep(0.1)
    kbd.release('c')
    kbd.release(keyboard.Key.ctrl_l)

def _f1():
    #按下f1
    kbd.press(keyboard.Key.f1)
    time.sleep(0.1)
    kbd.release(keyboard.Key.f1)

def on_press(key):
    if key==keyboard.Key.f2:
        execute()
def on_release(key):
    pass

def execute():
    #print("hello")
    # 复制
    _control_C()
    #粘贴
    mystr = pyperclip.paste()
    print('English：', mystr)
    # 翻译
    chinese_str = translateToChinese(mystr)
    sendMessageToWindow(chinese_str)
    #点击一下防止直接念英文
    mouse.click(pynput.mouse.Button.left)
    #朗读
    _f1()
    print('==='*30,'\n')


if __name__=="__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
