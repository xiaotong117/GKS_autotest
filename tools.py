#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests,time,os,base64
import configs
from urllib import quote
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

NULL = ""
ERROR_CODE = 0
SUCCESS_CODE = 1

# 方法列表：
# 打印开始日志    log_start(casename)
# 打印结束日志    log_end()
# 断言-判断结果   assertResult(self,result,targetvalue = SUCCESS_CODE)
# 断言-前后相同   assertEqual(self,first, second, msg='')
# 断言-前后不相同  assertNotEqual(self,first, second, msg='')
# 推送动作链功能   push_notification(cid,actionchain)
# 截图功能          screenshots(driver,casename)
# 查看校验日志        check_logs(driver,taskid,feedback)
# 验证文件是否存在  def verify_file(path,filsname)
# 双指滑动操作(找到元素左上角的坐标(x,y)，将(x+a,y+c)(x+b,y+c)两个点分别移动到(x+a,y+d)(x+b,y+d)      def double_slide(driver,elements,a,b,c,d)


def log_start(casename):
    print("\n********************************************************************")
    print("************************ " + casename + " ************************\n")

def log_end():
    print("\n************************ end ************************")
    print("**********************************************************************\n")

def assertResult(result,targetvalue = SUCCESS_CODE):
    if result != targetvalue:
        raise AssertionError('result:' + str(result))
    pass

def assertEqual(first, second, msg=''):
    if first != second:
        raise AssertionError(msg)
    pass

def assertNotEqual(first, second, msg=''):
    if first == second:
        raise AssertionError(msg)
    pass

# 推送动作链功能
def push_actionchain(cid,actionchain,extradata=''):
    s = requests.session()
    s.post(configs.URL1, data=configs.MYCOOKIE)
    r = s.post(configs.URL2%(cid,quote(str(actionchain))),quote(str(extradata)))
    time.sleep(3)
    # print actionchain
    # print (r.text)
    list = r.text.split(':')
    # print list
    messageID = list[1].strip()
    taskID = messageID.split('-')[2]
    print ("taskID = "+ taskID)
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

# 查看校验日志（可以验证多个回执）
def check_logs(driver,taskid,feedback):
    path = "/sdcard/libs/" + configs.PKG_name + "." + time.strftime("%Y-%m-%d", time.localtime()) + ".log" #文件路径/sdcard/libs/com.pp.infonew1.2018-06-21.log
    logsfile = driver.pull_file(path)
    logs = base64.b64decode(logsfile).decode('utf-8')#先解码byte转字符串，再用utf-8编码
    verify_pass = 0
    for i in feedback:
        SUCCESS_LOG = taskid + "|" + str(i)
        if SUCCESS_LOG in logs:
            verify_pass = verify_pass + 1
            continue
    if verify_pass == len(feedback):
        return SUCCESS_CODE
    else:
        return ERROR_CODE

# 验证文件是否存在(路径，文件名)
def verify_file(path,filsname):
    read = os.popen(path).readlines()
    for i in range(0, len(read)):
        # print read[i]
        # print filsname
        if read[i].strip() == filsname:
            return SUCCESS_CODE
    return ERROR_CODE

# 双指滑动操作(找到元素左上角的坐标(x,y)，将(x+a,y+c)(x+b,y+c)两个点分别移动到(x+a,y+d)(x+b,y+d)
def double_slide(driver,elements,a,b,c,d):
    title = driver.find_elements_by_id(elements)[0].location
    x = title["x"]
    y = title["y"]
    x1 = x + a
    x2 = x + b
    y1 = y + c
    y2 = y + d

    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    action3 = MultiAction(driver)
    action1.press(x=x1, y=y1).wait(500).move_to(x=x1, y=y2).wait(500).release()
    action2.press(x=x2, y=y1).wait(500).move_to(x=x2, y=y2).wait(500).release()
    action3.add(action1, action2)
    action3.perform()
    time.sleep(3)

# 清空通知列表
def clear_motification(driver):
    driver.open_notifications()
    time.sleep(3)
    ele1 = driver.find_elements_by_id("com.android.systemui:id/clear_all_button")
    ele2 = driver.find_elements_by_id("com.android.systemui:id/clear_notification")
    if len(ele1)|len(ele2):
        for e in ele1:
            e.click()
        for e in ele2:
            e.click()
    else:driver.open_notifications()

# 向上滑动屏幕
def swipeUp(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5     # x坐标
    y1 = l['height'] * 0.75   # 起始y坐标
    y2 = l['height'] * 0.25   # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

