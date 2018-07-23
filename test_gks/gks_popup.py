#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools, action_chain
from testbase import testbase
from urllib import quote
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_001_popup"
TITLE = "测试"
BTN_TEXT = "安装"
FEEDBACK = [0,1,40001]

class TestPopup(testbase):
    def __init__(self,driver,cid,appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 类型4
        actionchain1 = quote(str(action_chain.ACTIONCHAIN_POPUP%(self.appid, "4")))
        taskid1 = self.verify_actionchain(self.cid, actionchain1)

        self.verify_screenshots(CASE)

        self.verify_popup(self.driver, 4, TITLE, BTN_TEXT)

        self.verify_logs(taskid1, FEEDBACK)


        # 类型5
        actionchain2 = quote(str(action_chain.ACTIONCHAIN_POPUP % (self.appid, "5")))
        taskid2 = self.verify_actionchain(self.cid, actionchain2)

        self.verify_screenshots(CASE)

        self.verify_popup(self.driver, 5, TITLE, BTN_TEXT)

        self.verify_logs(taskid2, FEEDBACK)


        print(CASE + " 验证成功！")



