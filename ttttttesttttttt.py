#!/usr/bin/python2.7.5
# -*- coding: UTF-8 -*-

from appium import webdriver
import time,base64,requests,configs,action_chain
from urllib import quote
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
time.sleep(15)
# 获取cid和appid
cid = driver.find_element_by_id(configs.PKG_name + ":id/tvclientid").text
appidm = driver.find_element_by_id(configs.PKG_name + ":id/tvappid").text
appid = appidm.split("=")[1].strip()

print cid
print appid

driver.open_notifications()
time.sleep(3)
title = driver.find_elements_by_id('com.getui.lbs:id/getui_notification_icon')
for t in title:
    t.click()
pass

