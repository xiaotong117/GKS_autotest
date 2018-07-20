#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time,os,base64
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import configs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

NULL = ""
ERROR_CODE = 0
SUCCESS_CODE = 1

# 下拉查看并点击通知     pull_down_notification(driver,text)
# 点击banner通知    click_banner_notification(driver)
# banner+大图通知，点击通知  click_bigtype3_notification(driver)
# 验证popup弹框title和按钮文本，并点击按钮        popup_notification(driver,type,text1,text2)
# 通知样式6，双指下拉查看通知    double_pull_notification(driver,bigstyle)

# 下拉查看通知，查看到了之后点击通知
def pull_down_notification(driver,text):
    driver.open_notifications()
    time.sleep(3)
    title = driver.find_elements_by_class_name('android.widget.TextView')
    for t in title:
        if text == t.text:
            t.click()
            time.sleep(3)
            return SUCCESS_CODE
    return ERROR_CODE

# banner通知，点击通知
def click_banner_notification(driver):
    driver.open_notifications()
    time.sleep(3)
    title = driver.find_elements_by_id(configs.PKG_name + ':id/getui_notification_icon')
    for t in title:
        t.click()
        time.sleep(3)
    pass

# banner+大图通知，点击通知
def click_bigtype3_notification(driver):
    driver.open_notifications()
    time.sleep(3)
    title = driver.find_elements_by_id('com.android.systemui:id/backgroundNormal')
    le = len(title)-1
    title[le].click()
    time.sleep(3)
    pass

# 查看popup弹框，验证title和按钮文本，并点击
def popup_notification(driver,type,text1,text2):
    x = 0
    y = 0
    if type == 4:
        title1 = driver.find_elements_by_class_name('android.widget.TextView')
        for t in title1:
            if text1 == t.text:
                x += 1
                break
        title2 = driver.find_elements_by_class_name('android.widget.Button')
        for t in title2:
            if text2 == t.text:
                x += 1
                t.click()
                time.sleep(3)
                break
        if x == 2:
            return SUCCESS_CODE
        else: return ERROR_CODE

    if type == 5:
        title2 = driver.find_elements_by_class_name('android.widget.Button')
        for t in title2:
            if text2 == t.text:
                y += 1
                t.click()
                time.sleep(3)
                break
        if y == 1:
            return SUCCESS_CODE
        else: return ERROR_CODE

# 通知样式6，双指下拉查看通知
def double_pull_notification(driver,bigstyle):
    driver.open_notifications()
    time.sleep(3)

    if  not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_bigview_defaultView')):
        title = driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_notification_icon')[0].location
        x = title["x"]
        y = title["y"]
        x1 = x + 100
        x2 = x + 200
        y1 = y + 30
        y2 = y + 100

        action1 = TouchAction(driver)
        action2 = TouchAction(driver)
        action1.press(x=x1, y=y1).wait(500).move_to(x=x1, y=y2).wait(500).release()
        action2.press(x=x2, y=y1).wait(500).move_to(x=x2, y=y2).wait(500).release()
        MultiAction(driver).add(action1, action2).perform()
