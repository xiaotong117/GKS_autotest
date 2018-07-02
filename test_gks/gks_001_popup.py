#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver

class TestPopup:
    def __init__(self,cid,appid):
        self.cid = cid
        self.appid = appid
        pass

    def run(self):
        print("cid = " + self.cid)
        print("appid = " + self.appid)
