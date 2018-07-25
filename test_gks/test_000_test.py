#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "test_000_test"
TITLE = "测试"
FEEDBACK = [0,1,100]

class Test(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 下拉通知栏，清空所有通知
        tools.clear_motification(self.driver)

        # 推送动作连
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN%(self.appid))


        # 1.截图过程
        self.driver.open_notifications()
        time.sleep(2)
        self.verify_screenshots(CASE)

        # 2.下拉查看通知并点击
        self.verify_nitification(TITLE)

        # 3.查看日志
        self.verify_logs(taskid, FEEDBACK)

        print(CASE + " 验证成功！")
