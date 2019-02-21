# coding=utf-8
from pc_test_tool import *
from pywinauto import Desktop

window = Desktop(backend="uia").window(title=u'哆啦宝')
window.print_ctrl_ids()


def mouse_o():
    mouse_over(window, left=0, top=0)


def one_click():
    pass


def double_click():
    pass




if __name__ == "__main__":
    mouse_o()
    # one_click()
    # double_click()
