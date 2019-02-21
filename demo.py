# coding=utf-8
from subprocess import Popen
from pywinauto import Desktop
from pc_test_tool import *

Popen(r"D:\Program Files\DuoLaBao\bin\BasePay.exe", shell=True)
window = Desktop(backend="uia").window(title=u'哆啦宝')
# window.print_ctrl_ids()
# window.print_control_identifiers()
# a=window.criteria
window.child_window(auto_id="devSetTable").print_ctrl_ids()

b = window.window()
# 设备类型选择按钮
click_action(window, left=410, top=10)
# 意锐小盒-基础版
click_action(window, left=380, top=40)

# 设备类型选择按钮
click_action(window, left=410, top=10)
# 意锐小盒-基础版
click_action(window, left=380, top=60)

# pyautogui.press('shift')

# 设备类型选择按钮
click_action(window, left=410, top=10)
# 意锐小盒-基础版
click_action(window, left=380, top=80)
