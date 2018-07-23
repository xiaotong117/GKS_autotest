#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time,os,base64,tools,action_chain
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import configs
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

NULL = ""
ERROR_CODE = 0
SUCCESS_CODE = 1

class testbase:
    def __init__(self, driver):
        self.driver = driver

    def find_class_name(self, driver, class_name, result):
        title = driver.find_elements_by_class_name(class_name)
        for t in title:
            if result == t.text:
                t.click()
                time.sleep(3)
                return SUCCESS_CODE
        return ERROR_CODE

    def find_id(self, driver, id, result):
        title = driver.find_elements_by_class_name(id)
        for t in title:
            if result == t.text:
                t.click()
                time.sleep(3)
                return SUCCESS_CODE
        return ERROR_CODE

    def verify_actionchain(self,cid,actionchain):
        taskid = tools.push_actionchain(cid,actionchain)
        tools.assertNotEqual(self, taskid, tools.NULL, "动作连发送失败！")
        print "动作连发送成功！"
        print taskid

    # 下拉查看通知，查看到了之后点击通知
    def pull_down_notification(self, driver, text):
        driver.open_notifications()
        time.sleep(3)
        if self.find_class_name(driver, 'android.widget.TextView', text):
            return SUCCESS_CODE
        else:
            return ERROR_CODE

    # banner通知，点击通知
    def click_banner_notification(self, driver):
        driver.open_notifications()
        time.sleep(3)
        title = driver.find_elements_by_id(configs.PKG_name + ':id/getui_notification_icon')
        for t in title:
            t.click()
            time.sleep(3)
        pass

    # banner+大图通知，点击通知
    def click_bigtype3_notification(self, driver):
        driver.open_notifications()
        time.sleep(3)
        title = driver.find_elements_by_id('com.android.systemui:id/backgroundNormal')
        le = len(title) - 1
        title[le].click()
        time.sleep(3)
        pass

    # 查看popup弹框，验证title和按钮文本，并点击
    def popup_notification(self, driver, type, title_text, btn_text):
        result_btn = self.find_class_name(driver, 'android.widget.Button', btn_text)
        if type == 4:
            result_text = self.find_class_name(driver, 'android.widget.TextView', title_text)
            return result_btn & result_text
        return result_btn

    # 通知样式6，双指下拉查看通知
    def double_pull_notification(self, driver, bigstyle):
        driver.open_notifications()
        time.sleep(3)

        if not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_bigview_defaultView')):
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