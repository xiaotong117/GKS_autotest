#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time,os,base64
import configs
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

class testbase(unittest.TestCase):
    def __init__(self, driver):
        self.count = 0
        self.driver = driver
        self.pushconfig = pushconfig()
        self.initpushconfig()
        self.result = errorcode.doing
        self.isfetchcid = False
        pass
