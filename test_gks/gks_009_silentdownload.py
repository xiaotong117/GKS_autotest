#!/usr/bin/python
# -*- coding: utf-8 -*-

import tools,time,action_chain
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CASE = "gks_009_silentdownload"
NAME = "直接下载"
FEEDBACK = [0,1,10050,10060,10070,10080,10090]

class TestSilentdownload:
    def __init__(self, driver, cid, appid):
        self.driver = driver
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        # 1.删除文件夹中的文件，删除要安装的APP
        # 2.下发动作连
        # 3.验证下载文件
        # 4.点击安装
        # 5.检查APP安装完成后是否自动打开
        # 6.验证回执
        pass