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
ACTIONCHAIN_SILENTDOWNLOAD = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"appstartupid":{"android":"com.ibox.flashlight","ios":"sina","symbian":"0x27000000"},"stype":"gks_silentdownload","is_autostart":"true","name":"直接下载","actionid":"1","logo":"http://wap.igexin.com/img/logo.png","do":"100","is_autoinstall":"true","url":"http://imtt.dd.qq.com/16891/A97684073377D0D4D397FC06F21A3B97.apk"},{"actionid":"100","type":"null"}]}'

# 普通下载   %s为appid
ACTIONCHAIN_APPDOWNLOAD = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"appstartupid":{"android":"com.ibox.flashlight","ios":"sina","symbian":"0x27000000"},"stype":"gks_appdownload","is_autostart":"true","name":"直接下载","actionid":"1","logo":"http://wap.igexin.com/img/logo.png ","do":"100","is_autoinstall":"false","url":"http://imtt.dd.qq.com/16891/A97684073377D0D4D397FC06F21A3B97.apk"},{"actionid":"100","type":"null"}]}'

# 打开网页   %s为appid
ACTIONCHAIN_START_ANY_WEB = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"stype":"gks_startanyweb","forcescreenon":"true","actionid":"1","blacklist":"","whitelist":"com.UCMobile","do":"100","url":"http://www.igexin.com/"},{"actionid":"100","type":"null"},{"actionid":"100","type":"null"}]}'

# 热投消息 %s为appid
ACTIONCHAIN_TRANSMISSION = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"appstartupid":{"android":"com.sina.weibo","ios":"sina","symbian":"0x27000000"},"appid":"4bf8289fa3bcc0d44a0c9b49521b5a26","is_autostart":"false","actionid":"1","do":"100","type":"startapp","noinstall_action":"4"},{"actionid":"100","type":"null"}]}'

# 热投样式一透传内容 %s为taskid、cid
EXTRADATA_TRANSMISSION1 = '{"action":"notification","taskid":"%s","messageid":"MESSAGEID","cid":"%s","deviceid":"ANDROID-09309950e8e545dda88578b6465298ef","adlist":{"adid1":{"pkglist":["com.getui.lbs"],"ignoreLogo":"true","need_group":"false","banner":"http://imgsrc.baidu.com/forum/w%3D580/sign=3095a34a9b2f07085f052a08d924b865/218589950a7b0208ccb78ee467d9f2d3572cc839.jpg","dist":{"type":0,"params":["20"]},"title":"银泰优惠信息","url":"http://www.baidu.com","need_network":true,"notifystyle":1,"logo":"http://pic-pub.qiniudn.com/sina.png","fallback_browser":true,"text":"最新银泰优惠信息","showOccasion":2,"secondIconUrl":"@url:http://s1.hao123img.com/res/images/search_logo/image.png","click_url":["http%3a%2f%2fe.cn.miaozhen.com%2fr%2fk%3d2013091%26p%3d6wtxI%26dx%3d0%26ni%3d__IESID__%26mo%3d__OS__%26ns%3d__IP__%26m0%3d__OPENUDID__%26m0a%3d__DUID__%26m1%3d__ANDROIDID1__%26m1a%3d__ANDROIDID__%26m2%3d__IMEI__%26m4%3d__AAID__%26m5%3d__IDFA__%26m6%3d__MAC1__%26m6a%3d__MAC__%26nd%3d__DRA__%26np%3d__POS__%26nn%3d__APP__%26o%3d"],"self_first":true,"show_url":["http://track.data.getui.com/exp?k=3fdfc620a6da075d&p=d2307ad02f55c931"]}}}'

# 热投样式四透传内容 %s为taskid、cid
EXTRADATA_TRANSMISSION4 = '{"action":"notification","taskid":"%s","messageid":"MESSAGEID","cid":"%s","deviceid":"ANDROID-09309950e8e545dda88578b6465298ef","adlist":{"adid1":{"notifystyle":4,"pkglist":["com.getui.lbs"],"logo":"http://pic-pub.qiniudn.com/sina.png","banner":"http://imgsrc.baidu.com/forum/w%3D580/sign=3095a34a9b2f07085f052a08d924b865/218589950a7b0208ccb78ee467d9f2d3572cc839.jpg","fallback_browser":true,"text":"暴风测试1","title":"暴风测试1","secondIconUrl":"@url:http://7d9r6p.com1.z0.glb.clouddn.com/ad/adlogo.png","click_url":["http%3a%2f%2fe.cn.miaozhen.com%2fr%2fk%3d2013091%26p%3d6wtxI%26dx%3d0%26ni%3d__IESID__%26mo%3d__OS__%26ns%3d__IP__%26m0%3d__OPENUDID__%26m0a%3d__DUID__%26m1%3d__ANDROIDID1__%26m1a%3d__ANDROIDID__%26m2%3d__IMEI__%26m4%3d__AAID__%26m5%3d__IDFA__%26m6%3d__MAC1__%26m6a%3d__MAC__%26nd%3d__DRA__%26np%3d__POS__%26nn%3d__APP__%26o%3d","http://www.163.com"],"url":"http://www.baidu.com","self_first":true,"show_url":["http://www.qq.com","http://www.sina.com.cn"]}}}'

# 热投样式五透传内容 %s为taskid、cid
EXTRADATA_TRANSMISSION5 = '{"action":"notification","taskid":"%s","messageid":"MESSAGEID","cid":"%s","deviceid":"ANDROID-09309950e8e545dda88578b6465298ef","adlist":{"adid1":{"notifystyle":5,"pkglist":["com.sina.weibo"],"logo":"http://pic-pub.qiniudn.com/sina.png","banner":"http://imgsrc.baidu.com/forum/w%3D580/sign=3095a34a9b2f07085f052a08d924b865/218589950a7b0208ccb78ee467d9f2d3572cc839.jpg","fallback_browser":true,"text":"暴风测试1","title":"暴风测试1","secondIconUrl":"@url:http://7d9r6p.com1.z0.glb.clouddn.com/ad/adlogo.png","click_url":["http%3a%2f%2fe.cn.miaozhen.com%2fr%2fk%3d2013091%26p%3d6wtxI%26dx%3d0%26ni%3d__IESID__%26mo%3d__OS__%26ns%3d__IP__%26m0%3d__OPENUDID__%26m0a%3d__DUID__%26m1%3d__ANDROIDID1__%26m1a%3d__ANDROIDID__%26m2%3d__IMEI__%26m4%3d__AAID__%26m5%3d__IDFA__%26m6%3d__MAC1__%26m6a%3d__MAC__%26nd%3d__DRA__%26np%3d__POS__%26nn%3d__APP__%26o%3d","http://www.163.com"],"url":"http://www.baidu.com","self_first":true,"show_url":["http://www.qq.com","http://www.sina.com.cn"]}}}'

# 布局判断 %s为appid、布局类型
ACTIONCHAIN_CHECKLAYOUT = '{"action":"pushmessage","appkey":"110000","appid":"%s","id":"cmdid","messageid":"11111","taskid":"TASK_ID","push_info":{"action_key":"确定","badge":"1","sound":"cow.caf","message":"message"},"action_chains":[{"do_failed":"1002","stype":"gks_checklayout","actionid":"1","layoutType":%s,"do":"1001"},{"notifyStyle":1,"second_icon_url":"@package:com.getui.demo.dev","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"notification","actionid":"1001","logo":"demo.png","text":"正确","do":"100","title":"布局检测","timestamp":true},{"notifyStyle":1,"second_icon_url":"@package:com.getui.demo.dev","logo_url":"http://s1.hao123img.com/res/images/search_logo/image.png","stype":"notification","actionid":"1002","logo":"demo.png","text":"错误","do":"100","title":"布局检测","timestamp":true},{"actionid":"100","type":"null"}]}'

# app更新 %s为appid
ACTIONCHAIN_UPDATEAPP = ''
