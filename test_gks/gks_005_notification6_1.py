#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_005_notification6_1"
TITLE = "测试"
FEEDBACK = [0,1,30001,30011]

class TestNotification6_1:
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 下拉通知栏，清空所有通知
        # self.driver.open_notifications()
        # ele = self.driver.find_elements_by_id("com.android.systemui:id/clear_all_button")
        # for e in ele:
        #     e.click()

        # 推送动作连
        taskid = tools.push_actionchain(self.cid,action_chain.ACTIONCHAIN_NOTIFY6_1%(self.appid))
        tools.assertNotEqual(taskid, tools.NULL, "动作连发送失败！")
        print "动作连发送成功！"
        print taskid

        # 1.截图过程
        self.driver.open_notifications()
        time.sleep(2)
        result1 = tools.screenshots(self.driver,CASE)
        self.driver.open_notifications()
        time.sleep(2)
        tools.assertEqual(result1, tools.SUCCESS_CODE, "截图失败！")
        print "截图成功！"

        # 2.下拉查看通知并点击
        result2 = tools.pull_down_nitification(self.driver, TITLE)
        tools.assertEqual(result2, tools.SUCCESS_CODE, "通知验证失败！")
        print "通知验证成功！"

        # 3.查看日志
        result3 = tools.check_logs(self.driver,taskid,FEEDBACK)
        tools.assertEqual(result3, tools.SUCCESS_CODE, "日志验证失败！\n")
        print "日志验证成功！\n"

        print(CASE + " 验证成功！")