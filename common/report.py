#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-11-08 09:10:28
# @Last Modified time: 2018-11-08 09:11:13
# @E-mail: 1370465454@qq.com
# @Description:
def report(report_path):
    '''输出HTML报告到相应文件夹
    :report_path 测试报告的路径
    '''
    if len(sys.argv) > 1:
        report_name = os.getcwd() + '\\test_result\\test_report\\' + \
            sys.argv[1] + '_result.html'
    else:
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        reportname = os.getcwd() + '\\test_result\\test_report\\' + now + 'result.html'
        return reportname
