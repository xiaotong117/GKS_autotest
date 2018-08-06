#!/usr/bin/python2.7.5
# -*- coding: UTF-8 -*- 

from appium import webdriver
import HTMLTestRunner
import time,unittest,action_chain


# 一开始导入文件时报错无此模块，在test_gks目录下新建__init__.py文件，内容为空
import tools
import configs
from test_gks.test_000_test import Test
from test_gks.gks_popup import TestPopup
from test_gks.gks_notification import TestNotification
from test_gks.gks_download import TestAppdownload
from test_gks.gks_startanyweb import Startanyweb
from test_gks.gks_transmission import TestTransmission
from test_gks.gks_checklayout import TestChecklayout
from test_gks.gks_updateapp import TestUpdateapp
from test_gks.gks_gwa import Gwa
from test_gks.gks_filescan import Filescan



import sys

reload(sys)
sys.setdefaultencoding('utf8')

class GKS_Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 手机平台
        desired_caps['platformVersion'] = '5.1'  # 安卓版本，这里要根据自己手机进行修改
        desired_caps['deviceName'] = '16a94b82'  # 设备名称，通过adb devices获取
        desired_caps['appPackage'] = configs.PKG_name  # 要打开的app名称
        desired_caps['appActivity'] = configs.PKG_name + '.GetuiSdkDemoActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4727/wd/hub', desired_caps)
        time.sleep(15)
        # 获取cid和appid
        self.cid = self.driver.find_element_by_id(configs.PKG_name + ":id/tvclientid").text
        appidm = self.driver.find_element_by_id(configs.PKG_name + ":id/tvappid").text
        self.appid = appidm.split("=")[1].strip()

        if self.cid.strip() == '':
            print("cid 获取失败！！！")
        else:
            print("cid = " + self.cid)

        if self.appid.strip() == '':
            print("appid 获取失败！！！")
        else:
            print("appid = " + self.appid)

    def tearDown(self):
        self.driver.quit()

    # 测试，系统通知
    def test_000_test(self):
        # 打印开头日志
        tools.log_start("test_000_test")
        # 运行测例
        Test(self.driver,self.cid,self.appid).run()
        # 打印结束日志
        tools.log_end()

    # 测例1：popup弹框
    def test_001_popup(self):
        # 打印开头日志
        tools.log_start("gks_001_popup")
        # 运行测例
        TestPopup(self.driver,self.cid,self.appid).run()
        # 打印结束日志
        tools.log_end()

    # 测例2：notification 0 系统样式
    def test_002_notification0(self):
        # 打印开头日志
        tools.log_start("gks_002_notification0")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(0, action_chain.ACTIONCHAIN_NOTIFY0 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例3：notification 1 样式1
    def test_003_notification1(self):
        # 打印开头日志
        tools.log_start("gks_003_notification0")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(1, action_chain.ACTIONCHAIN_NOTIFY1 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例4：notification 4 样式4
    def test_004_notification4(self):
        # 打印开头日志
        tools.log_start("test_004_notification4")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(4, action_chain.ACTIONCHAIN_NOTIFY4 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例5：notification 6 样式6-1
    def test_005_notification6_1(self):
        # 打印开头日志
        tools.log_start("test_005_notification6_1")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(61, action_chain.ACTIONCHAIN_NOTIFY6_1 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例6：notification 6 样式6-2
    def test_006_notification6_2(self):
        # 打印开头日志
        tools.log_start("test_006_notification6_2")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(62, action_chain.ACTIONCHAIN_NOTIFY6_2 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例7：notification 6 样式6-3
    def test_007_notification6_3(self):
        # 打印开头日志
        tools.log_start("test_007_notification6_3")
        # 运行测例
        TestNotification(self.driver,self.cid,self.appid).notification(63, action_chain.ACTIONCHAIN_NOTIFY6_3 % (self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例8：普通下载
    def test_008_appdownload(self):
        # 打印开头日志
        tools.log_start("test_008_appdownload")
        # 运行测例
        TestAppdownload(self.driver,self.cid,self.appid).appdownload()
        # 打印结束日志
        tools.log_end()

    # 测例9：静默下载
    def test_009_silentdownload(self):
        # 打印开头日志
        tools.log_start("test_009_silentdownload")
        # 运行测例
        TestAppdownload(self.driver,self.cid,self.appid).silentdownload()
        # 打印结束日志
        tools.log_end()

    # 测例10：打开网页
    def test_010_startanyweb(self):
        # 打印开头日志
        tools.log_start("test_010_startanyweb")
        # 运行测例
        Startanyweb(self.driver,self.cid,self.appid).run()
        # 打印结束日志
        tools.log_end()

    # 测例11：热投样式一
    def test_011_transmission1(self):
        # 打印开头日志
        tools.log_start("test_011_transmission1")
        # 运行测例
        taskid = time.localtime()
        TestTransmission(self.driver,self.cid,self.appid).transmission(1, action_chain.EXTRADATA_TRANSMISSION1%(taskid,self.appid))
        # 打印结束日志
        tools.log_end()

    # 测例12：热投样式四
    def test_012_transmission4(self):
        # 打印开头日志
        tools.log_start("test_012_transmission4")
        # 运行测例
        taskid = time.localtime()
        TestTransmission(self.driver,self.cid,self.appid).transmission(4, action_chain.EXTRADATA_TRANSMISSION1%(taskid,self.appid),taskid)
        # 打印结束日志
        tools.log_end()

    # 测例13：热投样式五
    def test_013_transmission5(self):
        # 打印开头日志
        tools.log_start("test_013_transmission5")
        # 运行测例
        taskid = int(time.time())
        TestTransmission(self.driver,self.cid,self.appid).transmission(5, action_chain.EXTRADATA_TRANSMISSION1%(taskid,self.appid),taskid)
        # 打印结束日志
        tools.log_end()

    # 测例14：布局检测
    def test_014_checklayout(self):
        # 打印开头日志
        tools.log_start("test_014_checklayout")
        # 运行测例
        TestChecklayout(self.driver,self.cid,self.appid).Checklayout()
        # 打印结束日志
        tools.log_end()

    # 测例15：app更新
    def test_015_updateapp(self):
        # 打印开头日志
        tools.log_start("test_015_updateapp")
        # 运行测例
        TestUpdateapp(self.driver,self.cid,self.appid).updateapp()
        # 打印结束日志
        tools.log_end()

    # 测例16：地震预警
    def test_016_gwa(self):
        # 打印开头日志
        tools.log_start("test_016_gwa")
        # 运行测例
        Gwa(self.driver,self.cid,self.appid).gwa()
        # 打印结束日志
        tools.log_end()

    # 测例17：文件查找
    def test_017_filescan(self):
        # 打印开头日志
        tools.log_start("test_017_filescan")
        # 运行测例
        Filescan(self.driver,self.cid,self.appid).run()
        # 打印结束日志
        tools.log_end()

