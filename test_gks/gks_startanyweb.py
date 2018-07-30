#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain,os
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_startanyweb"
FEEDBACK = [0,1,"32000|adPkg:com.UCMobile"]

class Startanyweb(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 1.检查com.UCMobile是否安装，如果没有安装进行安装
        if not self.driver.is_app_installed("com.UCMobile"):
            print "安装UC浏览器"
            self.driver.install_app("./UC.apk")

        # 2.推送动作连
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_START_ANY_WEB%(self.appid))

        # 3.验证前台app
        time.sleep(10)
        activity = os.popen('adb shell "dumpsys activity | grep mFocusedActivity"').read()
        if "com.UCMobile" in activity:
            print "网页打开成功！"
        else:
            raise AssertionError("网页打开失败！")

        # 4.截图过程
        self.verify_screenshots(CASE)

        # 5.查看日志
        self.verify_logs(taskid, FEEDBACK)

        print(CASE + " 验证成功！")
