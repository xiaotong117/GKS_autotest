#!/usr/bin/python2.7.5
# encoding=utf-8

from GKS_test import GKS_Test
import HTMLTestRunner
import time,unittest


if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(GKS_Test)
        logtime = time.strftime('%Y%m%d_%H%M%S', time.localtime())
        filename = "./test_reports/report_%s.html" % logtime  # 定义报告存放路径。
        fp = file(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='android GKS自动化测试',
                                               description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述

        runner.run(suite)  # 自动进行测试.