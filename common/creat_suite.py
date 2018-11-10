#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-11-08 09:10:00
# @Last Modified time: 2018-11-08 09:10:15
# @E-mail: 1370465454@qq.com
# @Description:
def create_suite():
    '''创建测试集'''
    TestSuite = unittest.TestSuite()  # 测试集
    test_dir = os.getcwd() + '\\test_case\\'
    suite = unittest.defaultTestLoader.discover(
        start_dir=test_dir, pattern='test*.py', top_level_dir=None)
    for test_case in suite:
        TestSuite.addTests(test_case)
    return TestSuite
