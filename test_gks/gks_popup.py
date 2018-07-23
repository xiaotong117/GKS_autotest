#!/usr/bin/python
# -*- coding: utf-8 -*-

import testbase, tools, action_chain
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
        taskid1 = tools.push_actionchain(self.cid,actionchain1)
        tools.assertNotEqual(taskid1, tools.NULL, "动作连1发送失败！")
        print "动作连1发送成功！"
        print taskid1

        result1 = tools.screenshots(self.driver, CASE)
        tools.assertEqual(result1, tools.SUCCESS_CODE, "截图1失败！")
        print "截图1成功！"

        result2 = self.popup_notification(self.driver, 4, TITLE, BTN_TEXT)
        tools.assertEqual(result2, tools.SUCCESS_CODE, "弹框1验证失败！")
        print "弹框1验证成功！"

        result3 = tools.check_logs(self.driver, taskid1, FEEDBACK)
        tools.assertEqual(result3, tools.SUCCESS_CODE, "日志1验证失败！\n")
        print "日志1验证成功！\n"


        # 类型5
        actionchain2 = quote(str(action_chain.ACTIONCHAIN_POPUP % (self.appid, "5")))
        taskid2 = tools.push_actionchain(self.cid,actionchain2)
        tools.assertNotEqual(taskid2, tools.NULL, "动作连2发送失败！")
        print "动作连2发送成功！"
        print taskid2

        result4 = tools.screenshots(self.driver, CASE)
        tools.assertEqual(result4, tools.SUCCESS_CODE, "截图2失败！")
        print "截图2成功！"

        result5 = self.popup_notification(self.driver, 5, TITLE, BTN_TEXT)
        tools.assertEqual(result5, tools.SUCCESS_CODE, "弹框2验证失败！")
        print "弹框1验证成功！"

        result6 = tools.check_logs(self.driver, taskid2, FEEDBACK)
        tools.assertEqual(result6, tools.SUCCESS_CODE, "日志2验证失败！\n")
        print "日志2验证成功！\n"


        print(CASE + " 验证成功！")



