#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,tools,time,action_chain,subprocess
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

NAME = "快手"
INSTALL = "安装"
FEEDBACK = [1,10060,40021,40022,40023,40024,40025,40026,40210,40211]

class TestUpdateapp(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def updateapp(self):
        # 下拉通知栏，清空所有通知
        tools.clear_motification(self.driver)

        # 1.安装低版本快手
        if self.driver.is_app_installed("com.UCMobile"):
            os.system("adb uninstall com.smile.gifmaker")
            time.sleep(5)
        self.driver.install_app("./UC.apk")
        time.sleep(5)
        print "安装低版本快手"

        # 2.下发动作链
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_UPDATEAPP%(self.appid))

        # 3.验证下载文件
        time.sleep(60)
        result = tools.verify_file("adb shell ls /sdcard/libs/tmp", NAME + ".apk")
        tools.assertEqual(result, tools.SUCCESS_CODE, "下载文件验证失败！")
        print "下载文件验证成功！"

        # 4.下拉通知栏截图
        time.sleep(3)
        self.driver.open_notifications()
        time.sleep(2)
        self.verify_screenshots("updateapp_notification")

        # 5.验证通知并点击通知
        self.verify_nitification(NAME)
        time.sleep(5)
        self.verify_screenshots("updateapp_popup")

        # 6.点击安装
        time.sleep(5)


        # 7.验证回执
        self.verify_logs(taskid1, FEEDBACK)

        print("app更新 验证成功！")

