#!/usr/bin/python2.7.5
# -*- coding: UTF-8 -*-

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import time,base64,requests,configs,action_chain,tools
from testbase import testbase
from urllib import quote
import sys

reload(sys)
sys.setdefaultencoding('utf8')

PKG_name = "com.getui.lbs"

desired_caps = {}
desired_caps['platformName'] = 'Android'  # 手机平台
desired_caps['platformVersion'] = '6.0'  # 安卓版本，这里要根据自己手机进行修改
desired_caps['deviceName'] = 'Y9K0215505009215'  # 设备名称，通过adb devices获取
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

# tools.push_actionchain(cid,action_chain.ACTIONCHAIN_NOTIFY6_1%(appid))



driver.open_notifications()
time.sleep(3)
if not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_notification_icon')):
    tools.double_slide(driver, configs.PKG_name + ':id/getui_notification_icon', 100, 200, 30, 100)



# if not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_bigview_expanded')):
#     tools.double_slide(driver, configs.PKG_name + ':id/getui_bigview_banner', 200, 400, 50, 150)
# bigimage = driver.find_elements_by_id(configs.PKG_name + ':id/getui_bigview_expanded')
# for b in bigimage:
#     b.click()
#     time.sleep(3)


# driver.open_notifications()
# time.sleep(3)
# title = driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_notification_icon')[0].location
# # for t in title:
# #     print t.location
# x = title["x"]
# y = title["y"]
#
# x1 = x + 100
# x2 = x + 200
# y1 = y + 30
# y2 = y - 100
#
#
# action1 = TouchAction(driver)
# action2 = TouchAction(driver)
# action1.press(x=x1,y=y1).wait(500).move_to(x=x1,y=y2).wait(500).release()
# action2.press(x=x2,y=y1).wait(500).move_to(x=x2,y=y2).wait(500).release()
#
# MultiAction(driver).add(action1, action2).perform()

