# -*- coding: utf-8 -*-

from behave import *
import time
import os
import allure

# 侧边栏相机按钮 com.smile.gifmaker:id/right_btn
# 一键开启 com.smile.gifmaker:id/grant_record_all_permission_btn
# 始终允许 com.android.packageinstaller:id/permission_allow_button
# 始终允许 com.android.packageinstaller:id/permission_allow_button

# 拍11秒 com.smile.gifmaker:id/record_btn_bg
# 下一步 com.smile.gifmaker:id/editor_sdk_player

# @given(u'允许授权')
# def authorization(context):
#     time.sleep(2)
#     context.driver(text="始终允许").click()
#
# @given(u'我知道了')
# def know(context):
#     # path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/screenshot/'
#     context.driver.screenshot("home1.png")
#     time.sleep(5)
#     context.driver(text="我知道了").click()
#     time.sleep(1)
#     # os.chdir(path)
#     time.sleep(1)
#     context.driver.screenshot("home2.png")



# def save_photo(context,udid):
#     path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/behave-uiautomator2/screenshot/'
#     context.driver.screenshot(udid+"")





@given(u'登录')
def login(context):
    time.sleep(2)
    context.driver(text="登录").click()

@given(u'其他登录方式')
def login(context):
    time.sleep(2)
    context.driver(text="其他登录方式").click()
    # context.driver.screenshot("home1.png")

@given(u'点击邮箱')
def mail(context):
    time.sleep(2)
    context.driver(resourceId="com.smile.gifmaker:id/mail_login_view").click()


@given(u'输入框')
def click(context):
    time.sleep(2)
    context.driver(resourceId="com.smile.gifmaker:id/login_name_et").click()

@given(u'输入')
def input(context):
    time.sleep(2)
    context.driver.send_keys("datonggekwai9666@126.com")



# 始终允许

# 我知道了

# 登陆

# qq登陆

# 登陆


