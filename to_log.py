# coding=utf-8
import time


def to_log(text):
        with open("testLog.log", "r+", encoding='utf-8', errors='ignore') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(
                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ": " + text + '\n' + content)
            f.close()
        print(text)


