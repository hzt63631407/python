#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()                        # 线程1获得线程锁之后 print_time()会执行完全部 才释放锁 线程2才开始执行
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 3)
thread2 = myThread(2, "Thread-2", 4)

# 开启新线程
print("主线程")
thread1.start()
thread2.start()
print("主线程")

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"