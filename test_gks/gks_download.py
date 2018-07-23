#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,tools,time,action_chain
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_008_appdownload"
NAME = "直接下载"
FEEDBACK = [0,1,10050,10060,10070,10080,10090]

class TestAppdownload(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def appdownload(self):
        # 1.删除文件夹中的文件，删除要安装的APP
        os.system("adb shell rm -r /sdcard/libs/tmp")
        time.sleep(5)
        print "清空tmp文件夹"
        os.system("adb uninstall com.mas.wawagame.BDDKlord")
        time.sleep(10)
        print "删除要安装的APP"

        # 2.下发动作链
        taskid = tools.push_actionchain(self.cid, action_chain.ACTIONCHAIN_APPDOWNLOAD % (self.appid))
        tools.assertNotEqual(taskid, tools.NULL, "动作连发送失败！")
        print "动作连发送成功！"
        print taskid

        # 3.验证下载文件
        time.sleep(30)
        result1 = tools.verify_file("adb shell ls /sdcard/libs/tmp", NAME + ".pkg")
        tools.assertEqual(result1, tools.SUCCESS_CODE, "下载文件验证失败！")
        print "下载文件验证成功！"

        # 4.截图
        self.driver.open_notifications()
        time.sleep(2)
        result2 = tools.screenshots(self.driver, CASE)
        self.driver.open_notifications()
        time.sleep(2)
        tools.assertEqual(self, result2, tools.SUCCESS_CODE, "截图失败！")
        print "截图成功！"

        # 5.下拉通知栏验证通知并点击通知
        result3 = self.pull_down_nitification(self.driver, NAME)
        tools.assertEqual(result3, tools.SUCCESS_CODE, "通知验证失败！")
        print "通知验证成功！"

        # 6.点击安装

        # 7.检查APP安装完成后是否自动打开
        # 8.验证回执
        pass
    def silentdownload(self):
        # 1.删除文件夹中的文件，删除要安装的APP
        # 2.下发动作连
        # 3.验证下载文件
        # 4.点击安装
        # 5.检查APP安装完成后是否自动打开
        # 6.验证回执
        pass