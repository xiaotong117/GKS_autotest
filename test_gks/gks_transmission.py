#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain,os
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

TITLE = "银泰优惠信息"
FEEDBACK = [10000,10010,10040]


class TestTransmission(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def transmission(self, type, extra_data,taskid):
        # 下拉通知栏，清空所有通知
        tools.clear_motification(self.driver)

        # 推送动作连
        self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_TRANSMISSION%(self.appid),extra_data)

        # 1.截图过程
        if type==1 or type==4:
            self.driver.open_notifications()
            time.sleep(2)
            self.verify_screenshots("transmission" + str(type) + "-通知")

        # 2.下拉查看通知并点击
        if type == 1:
            self.verify_nitification(TITLE)
        elif type == 4:
            self.click_banner_notification(self.driver,"com.android.systemui:id/backgroundNormal")

        # 3.验证前台app
        time.sleep(10)
        activity = os.popen('adb shell "dumpsys activity | grep mFocusedActivity"').read()
        if "com.UCMobile" in activity:
            print "网页打开成功！"
        else:
            raise AssertionError("网页打开失败！")

        # 4.截图过程
        self.verify_screenshots("transmission" + str(type) + "-网页")

        # 5.查看日志---注意taskid---
        self.verify_logs(taskid+"|MESSAGEID", FEEDBACK)

        print("transmission" + str(type) + " 验证成功！")

