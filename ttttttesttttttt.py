#!/usr/bin/python2.7.5
# -*- coding: UTF-8 -*-

from appium import webdriver
import time,base64
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PKG_name = "com.getui.lbs"

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 手机平台
desired_caps['platformVersion'] = '4.1'  # 安卓版本，这里要根据自己手机进行修改
desired_caps['deviceName'] = '16a94b82'  # 设备名称，通过adb devices获取
desired_caps['appPackage'] = PKG_name  # 要打开的app名称
desired_caps['appActivity'] = 'com.getui.lbs.GetuiSdkDemoActivity'
driver = webdriver.Remote('http://127.0.0.1:4727/wd/hub', desired_caps)
time.sleep(1)
# 获取cid和appid
# cid = driver.find_element_by_id(PKG_name + ":id/tvclientid").text
# appidm = driver.find_element_by_id(PKG_name + ":id/tvappid").text
# appid = appidm.split("=")[1].strip()

path = "/sdcard/libs/com.getui.lbs.2018-07-05.log" #文件路径/sdcard/libs/com.pp.infonew1.2018-06-21.log
logsfile = driver.pull_file(path)
logs = base64.b64decode(logsfile).decode('utf-8')#先解码byte转字符串，再用utf-8编码
print logs
x = 0
feedback = [1,40001]
ss = "QAPOnrmt479FxOHbMfQ5o8"
for i in feedback:
    SUCCESS_LOG = ss + "|" + str(i)
    print SUCCESS_LOG
    print type(SUCCESS_LOG)
    if SUCCESS_LOG in logs:
        x = x + 1
        continue

print x
if x == len(feedback):
    print("回执验证成功！")
# if x == len(feedback):
#     print("回执验证成功！")
# else:
#     print("回执验证失败！")
