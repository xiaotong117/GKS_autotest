#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,tools,time,action_chain
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_008_appdownload"
NAME = "直接下载"
FEEDBACK = [0,1,10050,10060,10070,10080,10090]

class TestAppdownload:
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 1.删除文件夹中的文件，删除要安装的APP
        os.system("adb shell rm -r /sdcard/libs/tmp")
        time.sleep(5)
        print "清空tmp文件夹"
        os.system("adb uninstall com.mas.wawagame.BDDKlord")
        time.sleep(10)
        print "删除要安装的APP"

        # 2.下发动作链
        taskid = tools.push_notification(self.cid, action_chain.ACTIONCHAIN_APPDOWNLOAD % (self.appid))
        tools.assertNotEqual(taskid, tools.NULL, "动作连发送失败！")
        print "动作连发送成功！"
        print taskid

        # 3.验证下载文件
        time.sleep(30)
        read = os.popen('adb shell ls /sdcard/libs/tmp').readlines()
        result1 = 0
        for i in range(0, len(read)):
            # print read[i]
            if read[i].strip() == NAME + '.apk':
                result1 = 1
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
        result3 = tools.pull_down_nitification(self.driver, NAME)
        tools.assertEqual(result3, tools.SUCCESS_CODE, "通知验证失败！")
        print "通知验证成功！"

        # 6.点击安装

        # 7.检查APP安装完成后是否自动打开
        # 8.验证回执
        pass