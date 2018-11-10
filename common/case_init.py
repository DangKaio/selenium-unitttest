#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-30 15:15:07
# @Last Modified time: 2018-11-10 10:05:38
# @E-mail: 1370465454@qq.com
# @Description:
import unittest
import ddt
from .encapsulation import BasePage
from config import globalparam
from .log import Log
logger = Log()

@ddt.ddt
class Case_Test(unittest.TestCase):
    """测试之前的初始化"""
    driver = BasePage.browser(globalparam.browser)

    @classmethod  # 增加装饰器来满足每个用例浏览器一次启动一次退出
    def setUpClass(cls, dr=driver):
        cls.dr = dr
        cls.logger = logger
        cls.base_url = globalparam.base_url
        cls.logger.info(
            '############################### START ###############################')
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(30)
        cls.dr.verificationErrors = []
        cls.dr.accept_next_alert = True
        BasePage.open_url(cls,cls.base_url)

    @classmethod
    def tearDownClass(cls):
        cls.logger.info(
            '############################### END ###############################')
        # cls.driver.refresh()#将退出浏览器的操作变成刷新浏览器，用于不同用例之间的接洽操作
        # cls.dr.quit()
