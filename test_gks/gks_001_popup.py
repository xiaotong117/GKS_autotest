#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools
import configs

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

        taskid = tools.push_notification(self.cid,configs.ACTIONCHAIN_POPUP1(self.appid))

        # score = tools.pull_down_nitification(self.driver, TITLE)
        title = self.driver.find_elements_by_class_name('android.widget.TextView')[0]
        score = 0
        if TITLE.decode('utf-8') in title.text:
            score = 1

        btn = self.driver.find_elements_by_class_name('android.widget.Button')[0]
        if BTN_TEXT.decode('utf-8') in btn.text:
                score += 1


        # 2.截图过程
        tools.screenshots(self.driver, "test_001_popup")
        btn.click()
        tools.screenshots(self.driver, "test_001_popup")

        # 3.查看日志
        if tools.check_logs(self.driver, taskid, FEEDBACK) > 0:
            score += 1

        # 4.结果校验
        if score > 2:
            print("验证成功！")
        else:
            print("验证失败...")
            print(score)

        pass



