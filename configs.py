#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

PKG_name = "com.getui.lbs"
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
# 这里用到了转意符\
def ACTIONCHAIN_POPUP(appid,type):
    chain = '{"action":"pushmessage","appkey":"110000","appid":"' + appid.decode('utf-8') + '","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"btntext":"安装","popupstyle":' + str(type).decode('utf-8') + ',"bannerbg":"#1AA9AB","stype":"gks_popup","btncustomclick":"true","bannerurl":"http://img.xgo-img.com.cn/132_720x450/131034.jpg ","actionid":"1","whitelist":"honor,huawei,xiaomi,samsung,oppo","detail":"<h1><font color=\'#000000\'>详细信息</font></h1><br>通知管理功能升级：提供三种通知模式，接受不提醒，接受并提醒，屏蔽通知。自定义管理各类应用推送通知。<br><br>更新时间：2015.10.15<br>最新版本：6.7.1<br>大小：1.3M","do":"100","title":"测试"},{"actionid":"100","type":"null"}]}'
    return chain