#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain,configs
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

TITLE = "测试"
FEEDBACK = [0, 1, 30001, 30011]

class TestNotification(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def notification(self, type, action_chain):
        # 下拉通知栏，清空所有通知
        tools.clear_motification(self.driver)

        # 推送动作连
        taskid = self.verify_actionchain(self.cid, action_chain)

        # 1.截图过程
        self.driver.open_notifications()
        time.sleep(2)
        self.verify_screenshots("notification" + str(type))

        # 2.下拉查看通知并点击
        if type == 0 or type == 1:
            self.verify_nitification(TITLE)
        elif type == 4:
            self.click_banner_notification(self.driver,configs.PKG_name + ':id/getui_notification_icon')
        elif type == 61 or type == 62 or type == 63:
            self.double_pull_notification(self.driver, type, TITLE)

        # 3.查看日志
        self.verify_logs(taskid, FEEDBACK)

        print("notification" + str(type) + "验证成功！")