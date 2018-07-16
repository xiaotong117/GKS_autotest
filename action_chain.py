#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')


# Test主包原生通知   %s为appid
ACTIONCHAIN = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'

# popup弹框动作连     %s为appid   type类型      这里用到了转意符\      int类型转string类型 str(type)
ACTIONCHAIN_POPUP = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"btntext":"安装","popupstyle":%s,"bannerbg":"#1AA9AB","stype":"gks_popup","btncustomclick":"true","bannerurl":"http://img.xgo-img.com.cn/132_720x450/131034.jpg ","actionid":"1","whitelist":"honor,huawei,xiaomi,samsung,oppo","detail":"<h1><font color=\'#000000\'>详细信息</font></h1><br>通知管理功能升级：提供三种通知模式，接受不提醒，接受并提醒，屏蔽通知。自定义管理各类应用推送通知。<br><br>更新时间：2015.10.15<br>最新版本：6.7.1<br>大小：1.3M","do":"100","title":"测试"},{"actionid":"100","type":"null"}]}'

# 通知样式0 系统通知   %s为appid
ACTIONCHAIN_NOTIFY0 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":0,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png ","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"gks_notification","actionid":"1","logo":"demo.png","text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'

# 通知样式1 系统通知   %s为appid
ACTIONCHAIN_NOTIFY1 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":1,"second_icon_url":"@url:http://7d9r6p.com1.z0.glb.clouddn.com/ad/adlogo.png","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"gks_notification","actionid":"1","logo":"demo.png","isFloat":true,"text":"这个是图片","do":"100","title":"测试","timestamp":true},{"actionid":"100","type":"null"}]}'

# 通知样式4 系统通知   %s为appid
ACTIONCHAIN_NOTIFY4 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"notifyStyle":4,"second_icon_url":"@url:http://7d9r6p.com1.z0.glb.clouddn.com/ad/adlogo.png","logo_url":"","stype":"gks_notification","actionid":"1","logo":"demo.png","isFloat":true,"banner_url":"http://img.xgo-img.com.cn/132_720x450/131034.jpg","do":"100","timestamp":true},{"actionid":"100","type":"null"}]}'

# 通知样式6-1 系统通知   %s为appid
ACTIONCHAIN_NOTIFY6_1 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"gks_notification","isFloat":true,"do":"100","title":"测试","priority":"-1","notifyStyle":6,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png","actionid":"1","logo":"demo.png","text":"这个是图片","big_image_url":"http://img.xgo-img.com.cn/132_720x450/131034.jpg","bigStyle":"1","timestamp":true},{"actionid":"100","type":"null"}]}'

# 通知样式6-2 系统通知   %s为appid
ACTIONCHAIN_NOTIFY6_2 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"gks_notification","isFloat":true,"do":"100","title":"测试","priority":"-1","notifyStyle":6,"second_icon_url":"@url:http://s1.hao123img.com/res/images/search_logo/image.png","actionid":"1","logo":"demo.png","big_text":"刑警支队立即指派人带队赶赴茂名市，和茂名市公安局相关部门一起开展侦查和解救工作。由于绑匪具有极强的反侦察意识，不断更换电话、车辆，转移人质被关押地点，两地民警一天只休息一两个小时，连续几天和绑匪周旋。","text":"这个是图片","bigStyle":"2","timestamp":true},{"actionid":"100","type":"null"}]}'

# 通知样式6-3 系统通知   %s为appid
ACTIONCHAIN_NOTIFY6_3 = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"gks_notification","isFloat":true,"do":"100","priority":"-1","notifyStyle":6,"second_icon_url":"@url:http://wap.igexin.com/img/logo.png","actionid":"1","logo":"demo.png","banner_url":"http://img.xgo-img.com.cn/132_720x450/131034.jpg","big_image_url":"http://img.xgo-img.com.cn/132_720x450/131034.jpg","bigStyle":"3","timestamp":true},{"actionid":"100","type":"null"}]}'

# 静默下载   %s为appid
ACTIONCHAIN_SILENTDOWNLOAD = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"appstartupid":{"android":"com.mas.wawagame.BDDKlord","ios":"sina","symbian":"0x27000000"},"stype":"gks_silentdownload","is_autostart":"true","name":"直接下载","actionid":"1","logo":"http://wap.igexin.com/img/logo.png","do":"100","is_autoinstall":"true","url":"http://115.236.68.59:20820/222.apk"},{"actionid":"100","type":"null"}]}'

# 普通下载   %s为appid
ACTIONCHAIN_APPDOWNLOAD = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"appstartupid":{"android":"com.mas.wawagame.BDDKlord","ios":"sina","symbian":"0x27000000"},"stype":"gks_appdownload","is_autostart":"true","name":"直接下载","actionid":"1","logo":"http://wap.igexin.com/img/logo.png ","do":"100","is_autoinstall":"false","url":"http://115.236.68.59:20820/222.apk "},{"actionid":"100","type":"null"}]}'


