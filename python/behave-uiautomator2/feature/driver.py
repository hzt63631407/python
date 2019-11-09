# -*- coding: utf-8 -*-

import threading
import time

def meanwhile(d):
    while True:
        if d(resourceId="com.coloros.safecenter:id/et_login_passwd_edit"):
            print("次线程执行中")
            d(resourceId="com.coloros.safecenter:id/et_login_passwd_edit").set_text("tao126")
            d(text="安装").click()
            time.sleep(20)
            d(text="安装").click()
            time.sleep(60)
            # d.set_fastinput_ime(True)
            # d.set_text("tao126")
            # d.set_fastinput_ime(False)




