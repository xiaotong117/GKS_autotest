#!/usr/bin/python2.7.5
# -*- coding: UTF-8 -*- 

from appium import webdriver
import HTMLTestRunner
import time,unittest


# 一开始导入文件时报错无此模块，在test_gks目录下新建__init__.py文件，内容为空
import tools
import configs
from test_gks.gks_001_popup import TestPopup
from test_gks.test_000_test import Test
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class GKS_Test(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 手机平台
        desired_caps['platformVersion'] = '4.1'  # 安卓版本，这里要根据自己手机进行修改
        desired_caps['deviceName'] = '16a94b82'  # 设备名称，通过adb devices获取
        desired_caps['appPackage'] = configs.PKG_name  # 要打开的app名称
        desired_caps['appActivity'] = 'com.getui.lbs.GetuiSdkDemoActivity'
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
        tools.log_start("test_001_popup")
        # 运行测例
        TestPopup(self.driver,self.cid,self.appid).run()
        # 打印结束日志
        tools.end()


if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(GKS_Test)
        logtime = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        filename = "./test_reports/report_%s.html" % logtime  # 定义个报告存放路径，支持相对路径。
        fp = file(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='android SDK自动化测试',
                                               description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述

        runner.run(suite)  # 自动进行测试.