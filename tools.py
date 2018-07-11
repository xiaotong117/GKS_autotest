#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time,os,base64
import configs
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

NULL = ""
ERROR_CODE = 0
SUCCESS_CODE = 1

def log_start(casename):
    print("\n********************************************************************")
    print("************************ " + casename + " ************************\n")

def log_end():
    print("\n************************ end ************************")
    print("**********************************************************************\n")

def assertResult(self,result,targetvalue = SUCCESS_CODE):
    if result != targetvalue:
        raise AssertionError('result:' + str(result))
    pass

def assertEqual(self,first, second, msg=''):
    if first != second:
        raise AssertionError(msg)
    pass

def assertNotEqual(self,first, second, msg=''):
    if first == second:
        raise AssertionError(msg)
    pass

# 推送动作链功能
def push_notification(cid,actionchain):
    s = requests.session()
    s.post(configs.URL1, data=configs.MYCOOKIE)
    r = s.post(configs.URL2%(cid,actionchain))
    time.sleep(5)
    # print actionchain
    # print (r)
    list = r.text.split(':')
    # print (list[0])
    messageID = list[1].strip()
    taskID = messageID.split('-')[2]
    return taskID

# 截图功能
def screenshots(driver,casename):
    if not os.path.exists("./screenshots/"):
        # os.mkdir("./test_reports/screenshots/")   报错：[Error 3] :”系统找不到该路径”
        # mkdir只能在已存在的文件夹里创建子文件夹。如果想实现程序想要的直接创建多级目录的目标，则需要另外一个函数“makedirs”
        os.makedirs("./screenshots/")

    photo = "./screenshots/" + casename + "_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".png"
    driver.get_screenshot_as_file(photo)
    # 截图失败，不是同一级目录
    if os.path.exists(photo):
        return SUCCESS_CODE
    else:
        return ERROR_CODE

# 查看日志
def check_logs(driver,taskid,feedback):
    path = "/sdcard/libs/" + configs.PKG_name + "." + time.strftime("%Y-%m-%d", time.localtime()) + ".log" #文件路径/sdcard/libs/com.pp.infonew1.2018-06-21.log
    logsfile = driver.pull_file(path)
    logs = base64.b64decode(logsfile).decode('utf-8')#先解码byte转字符串，再用utf-8编码
    x = 0
    for i in feedback:
        SUCCESS_LOG = taskid + "|" + str(i)
        if SUCCESS_LOG in logs:
            x = x + 1
            continue
    if x == len(feedback):
        return SUCCESS_CODE
    else:
        return ERROR_CODE

# 下拉查看通知，查看到了之后点击通知
def pull_down_nitification(driver,text):
    driver.open_notifications()
    time.sleep(3)
    title = driver.find_elements_by_class_name('android.widget.TextView')
    for t in title:
        if text == t.text:
            t.click()
            time.sleep(3)
            return SUCCESS_CODE
    return ERROR_CODE

# banner通知，点击通知
def click_banner_nitification(driver):
    driver.open_notifications()
    time.sleep(3)
    title = driver.find_elements_by_id('com.getui.lbs:id/getui_notification_icon')
    for t in title:
        t.click()
        time.sleep(3)
    pass

# 查看popup弹框，验证title和按钮文本，并点击
def popup_nitification(driver,type,text1,text2):
    x = 0
    y = 0
    if type == 4:
        title1 = driver.find_elements_by_class_name('android.widget.TextView')
        for t in title1:
            if text1 == t.text:
                x += 1
                break
        title2 = driver.find_elements_by_class_name('android.widget.Button')
        for t in title2:
            if text2 == t.text:
                x += 1
                t.click()
                time.sleep(3)
                break
        if x == 2:
            return SUCCESS_CODE
        else: return ERROR_CODE

    if type == 5:
        title3 = driver.find_elements_by_class_name('android.widget.Button')
        for t in title3:
            if text2 == t.text:
                y += 1
                t.click()
                time.sleep(3)
                break
        if y == 1:
            return SUCCESS_CODE
        else: return ERROR_CODE