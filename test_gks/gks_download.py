#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,tools,time,action_chain,subprocess
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

NAME = "直接下载"
INSTALL = "安装"
FEEDBACK = [0,1,10050,10060,10070,10080,10090]

class TestAppdownload(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def appdownload(self):
        # 下拉通知栏，清空所有通知
        tools.clear_motification(self.driver)

        # 1.删除文件夹中的文件，删除要安装的APP
        subprocess.call('adb shell rm -r /sdcard/libs/tmp', shell=True)
        # import os
        # os.system("adb shell rm -r /sdcard/libs/tmp")
        time.sleep(5)
        print "清空tmp文件夹"
        os.system("adb uninstall com.ibox.flashlight")
        time.sleep(5)
        print "删除要安装的APP"

        # 2.下发动作链
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_APPDOWNLOAD % (self.appid))

        # 4.截图
        time.sleep(3)
        self.driver.open_notifications()
        time.sleep(2)
        self.verify_screenshots("appdownload")


        # 3.验证下载文件
        time.sleep(10)
        result = tools.verify_file("adb shell ls /sdcard/libs/tmp", NAME + ".apk")
        tools.assertEqual(result, tools.SUCCESS_CODE, "下载文件验证失败！")
        print "下载文件验证成功！"


        # 5.下拉通知栏验证通知并点击通知
        self.verify_nitification(NAME)

        # 6.点击安装
        butten = self.driver.find_elements_by_class_name("android.widget.Button")
        for b in butten:
            if INSTALL == b.text:
                b.click()
                time.sleep(15)

        # 7.检查APP安装完成后是否自动打开
        if "com.ibox.flashlight" in os.popen('adb shell "dumpsys activity | grep mFocusedActivity"').read() :
            print "下载文件验证成功！"
        else:print "下载文件验证失败！"

        # 8.验证回执
        self.verify_logs(taskid, FEEDBACK)

        print("普通下载 验证成功！")

    def silentdownload(self):
        # 1.删除文件夹中的文件，删除要安装的APP
        os.popen("adb shell rm -r /sdcard/libs/tmp")
        time.sleep(5)
        print "清空tmp文件夹"
        os.popen("adb uninstall com.ibox.flashlight")
        time.sleep(10)
        print "删除要安装的APP"

        # 2.下发动作连
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_SILENTDOWNLOAD % (self.appid))

        # 3.验证下载文件
        time.sleep(30)
        result = tools.verify_file("adb shell ls /sdcard/libs/tmp", NAME + ".pkg")
        tools.assertEqual(result, tools.SUCCESS_CODE, "下载文件验证失败！")
        print "下载文件验证成功！"

        # 4.点击安装
        butten = self.driver.find_elements_by_class_name("android.widget.Button")
        for b in butten:
            if INSTALL == b.text:
                b.click()
                time.sleep(15)

        # 5.检查APP安装完成后是否自动打开
        if "com.ibox.flashlight" in os.popen('adb shell "dumpsys activity | grep mFocusedActivity"').read() :
            print "下载文件验证成功！"
        else:print "下载文件验证失败！"

        # 6.验证回执
        self.verify_logs(taskid, FEEDBACK)

        print("静默下载 验证成功！")