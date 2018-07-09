#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools, action_chain
import sys

reload(sys)
sys.setdefaultencoding('utf8')

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
        title = self.driver.find_elements_by_class_name('android.widget.TextView')[0]
        score = 0
        if TITLE.decode('utf-8') in title.text:
            score = 1

        btn1 = self.driver.find_elements_by_class_name('android.widget.Button')[0]
        if BTN_TEXT.decode('utf-8') in btn1.text:
                score += 1

        tools.screenshots(self.driver, "test_001_popup1")

        # 类型5

        taskid2 = tools.push_notification(self.cid,action_chain.ACTIONCHAIN_POPUP(self.appid, "5"))
        btn2 = self.driver.find_elements_by_class_name('android.widget.Button')[0]
        if BTN_TEXT.decode('utf-8') in btn2.text:
            score += 1

        tools.screenshots(self.driver, "test_001_popup2")


        # 查看日志
        if tools.check_logs(self.driver, taskid1, FEEDBACK) > 0:
            score += 1
        if tools.check_logs(self.driver, taskid2, FEEDBACK) > 0:
            score += 1

        # 结果校验
        if score > 4:
            print("验证成功！")
        else:
            print("验证失败...")
            print(score)

        pass



