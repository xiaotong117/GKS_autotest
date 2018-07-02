#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
import tools
import configs

class TestPopup:
    def __init__(self,cid,appid):
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 推送动作连
        taskid = tools.push_notification(self.cid,self.appid,configs.ACTIONCHAIN_POPUP)
        # 1.下拉查看通知
        score = 0
        self.driver.open_notifications()
        title = self.driver.find_elements_by_class_name('android.widget.TextView')
        for t in title:
            if TITLE.decode('utf-8') in t.text:
                score += 1
                t.click()
                break

        #2.截图过程
        tools.screenshots(test_000_test)

        # 3.查看日志
        feedback = [1]
        if tools.check_logs(taskd,feedback) > 0:
            score += 1


        if score > 1:
            print("验证成功！")
        else :
            print("验证失败...")
            print(score)