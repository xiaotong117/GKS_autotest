#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools, action_chain
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_001_popup"
TITLE = "测试"
BTN_TEXT = "安装"
FEEDBACK = [0,1,40001]

class TestPopup:
    def __init__(self,driver,cid,appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        self.driver.open_notifications()
        ele = self.driver.find_elements_by_id("com.android.systemui:id/clear_all_button")
        for e in ele:
            e.click()

        # 类型4
        taskid1 = tools.push_notification(self.cid,action_chain.ACTIONCHAIN_POPUP%(self.appid, "4"))
        tools.assertNotEqual(self, taskid1, tools.NULL, "动作连1发送失败！")
        print "动作连1发送成功！"
        print taskid1

        result1 = tools.screenshots(self.driver, CASE)
        tools.assertEqual(self, result1, tools.SUCCESS_CODE, "截图1失败！")
        print "截图1成功！"

        result2 = tools.popup_nitification(self.driver, 4, TITLE, BTN_TEXT)
        tools.assertEqual(self, result2, tools.SUCCESS_CODE, "弹框1验证失败！")
        print "弹框1验证成功！"

        result3 = tools.check_logs(self.driver, taskid1, FEEDBACK)
        tools.assertEqual(self, result3, tools.SUCCESS_CODE, "日志1验证失败！")
        print "日志1验证成功！"

        # 类型5
        taskid2 = tools.push_notification(self.cid,action_chain.ACTIONCHAIN_POPUP(self.appid, "5"))
        tools.assertNotEqual(self, taskid2, tools.NULL, "动作连2发送失败！")
        print "动作连2发送成功！"
        print taskid2

        result4 = tools.screenshots(self.driver, CASE)
        tools.assertEqual(self, result4, tools.SUCCESS_CODE, "截图2失败！")
        print "截图2成功！"

        result5 = tools.popup_nitification(self.driver, 5, TITLE, BTN_TEXT)
        tools.assertEqual(self, result5, tools.SUCCESS_CODE, "弹框2验证失败！")
        print "弹框1验证成功！"

        result6 = tools.check_logs(self.driver, taskid2, FEEDBACK)
        tools.assertEqual(self, result6, tools.SUCCESS_CODE, "日志2验证失败！")
        print "日志2验证成功！"


        print(CASE + " 验证成功！")



