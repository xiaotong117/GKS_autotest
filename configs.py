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


# Test主包原生通知
def ACTIONCHAIN(appid):
    chain = '{"action":"pushmessage","appkey":"110000","appid":"' + appid.decode('utf-8') + '","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png ","stype":"notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'
    return chain

# popup弹框动作连
#ACTIONCHAIN_POPUP = '{"action":"pushmessage","appkey":"110000","appid":"' + appid.decode('utf-8') + '","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png ","stype":"notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'
