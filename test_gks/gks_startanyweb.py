#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain
from testbase import testbase
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_startanyweb"
FEEDBACK = [0,1,"32000|adPkg:com.UCMobile"]

class Startanyweb(testbase):
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 1.检查com.UCMobile是否安装，如果没有安装进行安装


        # 2.推送动作连
        taskid = self.verify_actionchain(self.cid, action_chain.ACTIONCHAIN_START_ANY_WEB%(self.appid))

        # 3.截图过程
        time.sleep(10)
        self.verify_screenshots(CASE)

        # 4.验证前台app，以及地址栏中的地址


        # 5.查看日志
        self.verify_logs(taskid, FEEDBACK)

        print(CASE + " 验证成功！")
