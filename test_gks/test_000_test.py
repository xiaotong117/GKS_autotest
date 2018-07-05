#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
import unittest
import tools
import configs

TITLE = "测试"
FEEDBACK = [0, 1, 100]

class Test(unittest.TestCase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 推送动作连
        taskid = tools.push_notification(self.cid,configs.ACTIONCHAIN(self.appid))

        # 1.下拉查看通知
        score = tools.pull_down_nitification(self.driver,TITLE)

        # 2.截图过程
        tools.screenshots("test_000_test")

        # 3.查看日志
        if tools.check_logs(taskid,FEEDBACK) > 0:
            score += 1

        # 4.结果校验
        if score > 1:
            print("验证成功！")
        else :
            print("验证失败...")
            print(score)