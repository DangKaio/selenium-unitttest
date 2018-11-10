#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-29 19:56:28
# @Last Modified time: 2018-11-10 14:13:50
# @E-mail: 1370465454@qq.com
# @Description:
import sys
import os
sys.path.append('../')
# prj_path = os.path.dirname(os.getcwd())
prj_path = os.path.dirname(os.path.dirname(__file__))
# 日志路径
log_path = os.path.join(prj_path, 'test_result', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'test_result', 'img_screenshot')
# HTML 测试报告路径
report_path = os.path.join(prj_path, 'test_result', 'test_report')
# 默认浏览器
browser = 'Chrome'
#驱动路径
driver_path=os.path.join(prj_path,'webdriver','chromedriver.exe')
# 浏览器地址
base_url = 'http:/*****'
# 上传文件路径(包括上传文件名+后缀)
upload_file_path = os.path.join(prj_path, 'test_data', 'file_upload')
# 下载路径
download_path = os.path.join(prj_path, 'test_data', 'file_download')
# 测试数据路径
data_path = os.path.join(prj_path, 'test_data', 'excel')
# 读取Excel数据
data_path_name = os.path.join(data_path, "templet.xlsx")
# 读取表名
read_excel_sheetname = "登录"
