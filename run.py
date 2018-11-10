#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-19 15:26:42
# @Last Modified time: 2018-11-07 15:41:50
# @E-mail: 1370465454@qq.com
# @Description:
import unittest
import sys
import os
from test_result.HTRunner.HTMLTestRunner3 import HTMLTestRunner
import time
from common import sendmail


def create_suite():
    '''创建测试集'''
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = os.getcwd() + '\\test_case\\'
    suite = unittest.defaultTestLoader.discover(
        start_dir=test_dir, pattern='test*.py', top_level_dir=None)
    for test_case in suite:
        TestSuite.addTests(test_case)
    return TestSuite


def report():
    '''输出HTML报告到相应文件夹'''
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\test_result\\test_report\\' + \
            sys.argv[1] + '_result.html'
    else:
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.getcwd() + '\\test_result\\test_report\\' + now + 'result.html'
        return reportname
fp = open(report(), 'wb')
runner = HTMLTestRunner(stream=fp, title=u'测试报告',
                        description=u'测试用例执行情况'
                        )

if __name__ == '__main__':
    TestSuite = create_suite()
    runner.run(TestSuite)
    # 发送邮件
    # mail = sendmail.Send_Mail()
    # mail.send()
    fp.close()
