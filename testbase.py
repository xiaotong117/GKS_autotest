#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest,time,os,base64,tools,action_chain
import configs
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

NULL = ""
ERROR_CODE = 0
SUCCESS_CODE = 1

class testbase(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def find_class_name(self, driver, class_name, result):
        title = driver.find_elements_by_class_name(class_name)
        for t in title:
            # print t.text
            # print result
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
        tools.assertNotEqual(taskid, tools.NULL, "动作连发送失败！")
        print "动作连发送成功！"
        return taskid

    def verify_screenshots(self,filename):
        result = tools.screenshots(self.driver,filename)
        tools.assertEqual(result, tools.SUCCESS_CODE, "截图失败！")
        print "截图成功！"

    def verify_nitification(self,text):
        result = self.find_class_name(self.driver, 'android.widget.TextView', text)
        tools.assertEqual(result, tools.SUCCESS_CODE, "通知验证失败！")
        print "通知验证成功！"

    def verify_logs(self, taskid, FEEDBACK):
        result = tools.check_logs(self.driver, taskid, FEEDBACK)
        tools.assertEqual(result, tools.SUCCESS_CODE, "日志验证失败！\n")
        print "日志验证成功！\n"

    def verify_popup(self,driver, type, title, btn_title):
        result = self.popup_notification(driver, type, title, btn_title)
        tools.assertEqual(result, tools.SUCCESS_CODE, "弹框验证失败！")
        print "弹框验证成功！"

    # 下拉查看通知，查看到了之后点击通知
    # def pull_down_notification(self, driver, text):
    #     driver.open_notifications()
    #     time.sleep(3)
    #     if self.find_class_name(driver, 'android.widget.TextView', text):
    #         return SUCCESS_CODE
    #     else:
    #         return ERROR_CODE

    # banner通知，点击通知
    def click_banner_notification(self, driver):
        title = driver.find_elements_by_id(configs.PKG_name + ':id/getui_notification_icon')
        for t in title:
            t.click()
            time.sleep(3)
        pass

    # 查看popup弹框，验证title和按钮文本，并点击
    def popup_notification(self, driver, type, title_text, btn_text):
        result_text = 1
        if type == 4:
            result_text = self.find_class_name(driver, 'android.widget.TextView', title_text)
        result_btn = self.find_class_name(driver, 'android.widget.Button', btn_text)
        return result_btn & result_text

    # 通知样式6，双指下拉查看通知
    def double_pull_notification(self, driver, bigstyle, text):
        if bigstyle ==61 or bigstyle ==62:
            if not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_big_notification_icon')):
                tools.double_slide(driver,configs.PKG_name + ':id/getui_notification_icon',100,200,30,100)
                time.sleep(3)
                self.verify_screenshots("notification" + str(type))
            result = self.find_class_name(driver, 'android.widget.TextView', text)
            tools.assertEqual(result, tools.SUCCESS_CODE, "通知验证失败！")
            print "通知验证成功！"

        if bigstyle ==63:
            if not len(driver.find_elements_by_id(configs.PKG_name + ':id/getui_bigview_expanded')):
                tools.double_slide(driver,configs.PKG_name + ':id/getui_bigview_banner',200,400,50,150)
                time.sleep(3)
                self.verify_screenshots("notification" + str(type))
            bigimage = driver.find_elements_by_id(configs.PKG_name + ':id/getui_bigview_expanded')
            for b in bigimage:
                b.click()
                time.sleep(3)


