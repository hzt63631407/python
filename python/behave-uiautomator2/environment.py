# -*- coding: utf-8 -*-
# behave feature/login.feature -fallure_behave.formatter:AllureFormatter -o ./reports/
# allure serve ./reports/
# /Users/huangzetao/PycharmProjects/untitled/venv/lib/python2.7/site-packages

# behave -Dudid=6e48b8db                    一加5
# behave -Dudid=926QADVU227Y5               魅族16xs
# oppo a59s uid IVGU55DELJSGFQZ5


import uiautomator2 as u2
import time
import os
import allure
from feature.driver import meanwhile
import threading


# path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/reports/'

def uninstall(packageName):
    os.popen("adb wait-for-device")
    print("start uninstall...")
    os.popen("adb uninstall %s" % packageName)


def install(filename):
    print("install...")
    os.popen("adb install %s" % filename)


def getDevicesAll():
    devices = []
    try:
        for dName_ in os.popen("adb devices"):
            if "\t" in dName_:
                if dName_.find("emulator") < 0:
                    devices.append(dName_.split("\t")[0])
        devices.sort(cmp=None, key=None, reverse=False)
    except:
        pass
    return devices


def save_screenshot(context, path, calling_request):
    os.chdir(path)
    context.driver.screenshot(calling_request + '.png')
    return os.path.join(path, calling_request + '.png')


def before_all(context):
    devices = getDevicesAll()
    #
    devices = str(devices[0])

    # devices = context.config.userdata["udid"]  # 正确写法

    d = u2.connect_usb(devices)

    context.driver = d

    timer = threading.Timer(2.0, meanwhile, [d])

    timer.start()

    time.sleep(5)

    print("主线程执行中")

    apk = "com.smile.gifmaker"

    uninstall(apk)

    #
    install("/Users/huangzetao/Desktop/快手app包/kwai-android-test-gifmakerhuidu-6.8.0.99999-huice.apk")

    # print("安装中1")
    #
    # time.sleep(5)
    #
    # d(resourceId="com.coloros.safecenter:id/et_login_passwd_edit").click()
    #
    # print("安装中2")
    #
    # time.sleep(2)
    #
    # d(text="安装").click()
    #
    # time.sleep(2)
    #
    # d(text="安装").click()

    d.app_start(apk)

    print("success")

    # os.chdir(path)

    # time.sleep(2)
    #
    # d(resourceId="com.smile.gifmaker:id/left_btn").click()
    #
    # time.sleep(1)
    #
    # d(resourceId="com.smile.gifmaker:id/tv_game_center").click()

    # path = os.path.join(path + ".png")
    #
    # allure.attach(path, attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    # path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/reports'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/'
    print("scenario:" + str(id(scenario)))
    # t = str(id(scenario))
    path = save_screenshot(context, path, str(id(scenario)))
    allure.attach.file(path, "截图", attachment_type=allure.attachment_type.PNG)
    # allure.attach.__call__()
    # allure.attach.file(t, "cpu", attachment_type=allure.attachment_type.STRING)
    # allure.attach.file(path, "截图", attachment_type=allure.attachment_type.PNG)



    # 2次
    # path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/screenshot/'
    # path = os.path.join(path + "home2.png")
    # allure.attach.file(path, "截图", attachment_type=allure.attachment_type.PNG)
    # allure.attach(path, "失败截图", attachment_type=allure.attachment_type.PNG)
