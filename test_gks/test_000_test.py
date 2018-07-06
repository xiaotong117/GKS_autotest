#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain

TITLE = "测试"
FEEDBACK = [0, 1, 100]

class Test:
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 下拉通知栏，清空所有通知
        self.driver.open_notifications()
        ele = self.driver.find_elements_by_id("com.android.systemui:id/clear_all_button")
        for e in ele:
            e.click()

        # 推送动作连
        taskid = tools.push_notification(self.cid,action_chain.ACTIONCHAIN(self.appid))

        # 1.下拉查看通知
        score = tools.pull_down_nitification(self.driver,TITLE)

        # 2.截图过程
        self.driver.open_notifications()
        time.sleep(2)
        tools.screenshots(self.driver,"test_000_test")

        # 3.查看日志
        if tools.check_logs(self.driver,taskid,FEEDBACK) > 0:
            score += 1

        # 4.结果校验
        if score > 1:
            print("验证成功！")
        else :
            print("验证失败...")
            print("score = " + str(score))