#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain,configs
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

FEEDBACK_TRUE = [0, 1, 1001, 30001]
FEEDBACK_FALSE = [0, 1, 1002, 30002]

class TestChecklayout(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def Checklayout(self):
        for type in [1,2,3,4]:
            print type
            # 下拉通知栏，清空所有通知
            tools.clear_motification(self.driver)

            # 推送动作连
            taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_CHECKLAYOUT(self.appid,str(type)))

            # 1.截图过程
            self.driver.open_notifications()
            time.sleep(2)
            self.verify_screenshots("checklayout" + str(type))

            # 2.下拉查看通知并点击，查看日志
            if type == 1 or type == 4:
                self.verify_nitification("错误")
                self.verify_logs(taskid, FEEDBACK_FALSE)
            elif type == 2 or type == 3:
                self.verify_nitification("正确")
                self.verify_logs(taskid, FEEDBACK_TRUE)

            print("checklayout" + str(type) + "验证成功！")


