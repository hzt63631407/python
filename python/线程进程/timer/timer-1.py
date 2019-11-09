# -*- coding: utf-8 -*-
# Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。

# https://blog.csdn.net/qq_32590631/article/details/81031556
# https://www.cnblogs.com/longsongpong/p/10997692.html

import threading
import time

def hello(name):
    print ("hello %s\n" ) % name
    # global timer
    # timer = threading.Timer(2.0, hello, ["Hawk"])   # 线程内部自己不断的调用
    # timer.start()
    time.sleep(1)
    print("1")
    time.sleep(2)
    print("2")
    time.sleep(3)
    print("3")

if __name__ == "__main__":
    timer = threading.Timer(2.0, hello, ["test"])   ## 每隔两秒调用函数hello
    timer.start()
    time.sleep(5)
    print("主线程")
