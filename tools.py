#!/usr/bin/python
# -*- coding: utf-8 -*-

from appium import webdriver
import requests,time,unittest,os,base64
import configs

def log_start(casename):
    print("************************************************")
    print("************ " + casename + " ************")

def log_end():
    print("************ end ************")
    print("************************************************")

# 推送动作连功能
def push_notification(cid,appid,actionchain):
    s = requests.session()
    s.post(configs.URL1, data=configs.MYCOOKIE)
    r = s.post(configs.URL2)
    list = r.text.split(':')
    taskID = list[1].strip()
    if taskID == "":
        print("动作连发送失败！")
    else：
        print("taskID = " + taskID)
    return taskID

# 截图功能
def screenshots(casename):
    if not os.path.exists("./screenshots/"):
        # os.mkdir("./test_reports/screenshots/")   报错：[Error 3] :”系统找不到该路径”
        # mkdir只能在已存在的文件夹里创建子文件夹。如果想实现程序想要的直接创建多级目录的目标，则需要另外一个函数“makedirs”
        os.makedirs("./screenshots/")
        self.driver.get_screenshot_as_file(
            "./screenshots/" + casename + "_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".png")
        # 截图失败，不是同一级目录

# 查看日志
def check_logs(taskid,feedback):
    path = "/sdcard/libs/" + configs.PKG_name + "." + time.strftime("%Y-%m-%d", time.localtime()) + ".log" #文件路径/sdcard/libs/com.pp.infonew1.2018-06-21.log
    logsfile = self.driver.pull_file(path)
    logs = base64.b64decode(logsfile).decode('utf-8')#先解码byte转字符串，再用utf-8编码
    x = 0
    for i in feedback:
        SUCCESS_LOG = taskid.decode('utf-8') + "|" + i
        if SUCCESS_LOG.decode('utf-8') in logs:
            x = x + 1
            continue
    if x == len(feedback):
        print("回执验证成功！")
        return 1
    else:
        print("回执验证失败！！")
        return 0

    # print("SUCCESS_LOG = " + SUCCESS_LOG)
    # for line in logs:
    #     print(line)
    #     if SUCCESS_LOG.decode('utf-8') in line:
    #         score += 1
    #         break
    if SUCCESS_LOG.decode('utf-8') in logs:
        score += 1
