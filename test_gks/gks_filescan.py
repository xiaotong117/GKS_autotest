#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain,os
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_filescan"
FEEDBACK = [0,1,100,10000,40700]

class Filescan(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        for rule in range(0,3):
            # 下拉通知栏，清空所有通知
            os.system("adb shell rm -r /sdcard/libs/filescan")
            time.sleep(3)
            os.system("adb shell mkdir -p /sdcard/libs/filescan")
            os.system("adb shell touch /sdcard/libs/filescan/12345.txt")

            # 推送动作连
            taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_FILESCAN%(rule,self.appid))

            # 查看日志
            self.verify_logs(taskid, FEEDBACK)

        print(CASE + " 验证成功！")

