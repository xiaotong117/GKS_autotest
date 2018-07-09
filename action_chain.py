#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')


# Test主包原生通知
# %s为appid
ACTIONCHAIN = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png ","stype":"notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'

# popup弹框动作连
# %s为appid   type类型
# 这里用到了转意符\
# int类型转string类型 str(type)
def ACTIONCHAIN_POPUP(appid,type):
    chain = '{"action":"pushmessage","appkey":"110000","appid":"' + appid.decode('utf-8') + '","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"btntext":"安装","popupstyle":' + str(type).decode('utf-8') + ',"bannerbg":"#1AA9AB","stype":"gks_popup","btncustomclick":"true","bannerurl":"http://img.xgo-img.com.cn/132_720x450/131034.jpg ","actionid":"1","whitelist":"honor,huawei,xiaomi,samsung,oppo","detail":"<h1><font color=\'#000000\'>详细信息</font></h1><br>通知管理功能升级：提供三种通知模式，接受不提醒，接受并提醒，屏蔽通知。自定义管理各类应用推送通知。<br><br>更新时间：2015.10.15<br>最新版本：6.7.1<br>大小：1.3M","do":"100","title":"测试"},{"actionid":"100","type":"null"}]}'
    return chain
ACTIONCHAIN_POPUP = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"btntext":"安装","popupstyle":%s.,"bannerbg":"#1AA9AB","stype":"gks_popup","btncustomclick":"true","bannerurl":"http://img.xgo-img.com.cn/132_720x450/131034.jpg ","actionid":"1","whitelist":"honor,huawei,xiaomi,samsung,oppo","detail":"<h1><font color=\'#000000\'>详细信息</font></h1><br>通知管理功能升级：提供三种通知模式，接受不提醒，接受并提醒，屏蔽通知。自定义管理各类应用推送通知。<br><br>更新时间：2015.10.15<br>最新版本：6.7.1<br>大小：1.3M","do":"100","title":"测试"},{"actionid":"100","type":"null"}]}'