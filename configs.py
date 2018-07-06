#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

PKG_name = "com.getui.lbs"

# 工具箱地址
MYCOOKIE = {'username': 'admin', 'password': 'Toolbox@getui2018!'}
URL1 = "http://172.16.14.130:8090/login.htm"

def URL2(cid,actionchain):
    url = 'http://172.16.14.130:8090/pushTest.htm?' + 'clientID=' + cid.decode('utf-8') + '&clientData=' + actionchain.decode('utf-8')
    return url.decode('utf-8')


