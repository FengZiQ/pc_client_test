#!usr/bin/python
# -*- coding: utf-8 -*-
from subprocess import Popen
from pywinauto import Desktop
import time
Popen('D:\Program Files\DuoLaBao\unins000.exe', shell=True)
time.sleep(2)
dlg = Desktop(backend="win32").window(title=u"哆啦宝 反安装")

# 界面一 您确定完全删除 哆啦宝 和相关组件吗?
# 获取路径输入框
dlg.type_keys("%Y")

# 界面二 哆啦宝 被成功地从您的电脑中删除。
# 发送快捷键 下一步
time.sleep(2)
dlgv = Desktop(backend="win32").window(title=u"哆啦宝 反安装")
buttonOk = u"确定"
dlgv[buttonOk].click()





