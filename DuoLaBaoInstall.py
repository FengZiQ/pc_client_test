#!usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import Popen
from pywinauto import Desktop
import FromPostion
import pyautogui
import time

def Install():
    Popen(r'D:\Client\DuoLaBao\Setup-DLB-1.4.12.1.exe', shell=True)
    time.sleep(1)
    dlg = Desktop(backend="win32").window(title=u"安装 - 哆啦宝")

    # 界面一 您将把哆啦宝安装在哪里?
    # 界面一 您将把哆啦宝安装在哪里?
    time.sleep(1)
    # 获取路径输入框
    dlg.window(class_name="TEdit")
    edit = dlg['TEdit']
    # 输入路径
    edit.set_text(r'D:\Program Files\DuoLaBao')
    # 发送快捷键 下一步
    dlg.type_keys("%N")

    # 文件夹已经存在
    # 文件夹已经存在
    time.sleep(2)
    exeits = Desktop(backend="win32").window(title=u"文件夹已经存在")
    #判断窗体是否存在
    if exeits.exists():
        exeits.type_keys("%Y")

    # 界面二 您想选择哪个附加任务?
    # 界面二 您想选择哪个附加任务?
    # 发送快捷键 下一步
    time.sleep(2)
    dlg.type_keys("%N")

    # 界面三 安装程序开始在您的电脑中安装哆啦宝.
    # 界面三 安装程序开始在您的电脑中安装哆啦宝.
    time.sleep(2)
    dlg.type_keys("%I")

    #界面四 哆啦宝安装完成F
    #界面四 哆啦宝安装完成F
    time.sleep(2)
    dlgss = Desktop(backend="win32").window(title=u"安装 - 哆啦宝")
    dlgss.type_keys("%F")

    # 界面五 初始化激活提示
    # 界面五 初始化激活提示
    time.sleep(3)
    dlgcc = Desktop(backend="uia").window(title=u"初始化激活提示")
    # 获取窗体坐标
    idc = FromPostion.GetZuoBiao(dlgcc)
    # print idc
    # 获取屏幕大小
    screenWidth, screenHeight = pyautogui.size()
    # 获取当前鼠标位置
    currentMouseX, currentMouseY = pyautogui.position()
    # 激活对话框窗体操作
    # 激活对话框窗体操作
    def TuiChu():
        time.sleep(1)
        # 移动鼠标到指定位置
        pyautogui.moveTo(idc[0] + 130, idc[1] + 150)
        # 鼠标点击事件
        pyautogui.click()
        return
    TuiChu()
    return
Install()



