#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')

PKG_name = "com.getui.lbs"

# 工具箱地址
MYCOOKIE = {'username': 'admin', 'password': 'Toolbox@getui2018!'}
URL1 = "http://172.16.14.130:8090/login.htm"

# 两个%s，一个为cid，一个为动作链
URL2 = "http://172.16.14.130:8090/pushTest.htm?clientID=%s&clientData=%s."


