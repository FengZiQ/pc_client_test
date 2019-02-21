# coding=utf-8
from findCoordinate import get_coordinate
from to_log import all_logs, testlink
import pyautogui
import time

Pass = "'result': 'p'"
Fail = "'result': 'f'"


# 点击操作
def click_action(window, left, top):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    pyautogui.click()
    time.sleep(2)
    return


# 鼠标悬停
def mouse_over(window, left, top):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    time.sleep(2)
    return


# 填充文本框操作0
def fill_in_text(window, left, top, text):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    pyautogui.click()
    pyautogui.typewrite(text)
    time.sleep(1)
    return


# 断言
def mark_status(flag):
    if flag:
        all_logs(Fail)
        testlink(Fail + '\n')
    else:
        all_logs(Pass)
        testlink(Pass + '\n')

