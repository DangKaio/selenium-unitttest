#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-30 15:32:12
# @Last Modified time: 2018-11-10 11:20:35
# @E-mail: 1370465454@qq.com
# @Description:
import sys
import ddt
sys.path.append('../')
from common import case_init
import unittest
from config.globalparam import data_path_name, read_excel_sheetname
from common.read_excel import ExcelUtil
testdata = ExcelUtil(data_path_name, read_excel_sheetname).dict_data()
from common.encapsulation import BasePage


@ddt.ddt
class Page_Login(case_init.Case_Test):
    # def test_success(self):
    #     '''登陆成功,username名字  password密码'''

    # @unittest.skip("I don't want to run this case.")
    def success(self, param):
        '''登陆成功,username名字  password密码'''
        print(type(param["Element"]))


        if param["Action"] == 'send_key':
            if type(param["Input"]) is float:
                BasePage.send_key(self,param["Type"], param["Element"], int(param["Input"]))
            else:
                BasePage.send_key(self,param["Type"], param["Element"], param["Input"])

        elif param["Action"] == 'click':
            BasePage.click_element(self,param["Type"], param["Element"])



        elif param["Action"] == "" or param["Action"] == "none":
            pass
        elif param["IsSkip"]=="skip":
            pass
        elif param["Action"] == "js" or param["Action"] == "jquery":
            pass
        else:
            self.logger.error("请在excel添加数据")

    @ddt.data(*testdata)
    # @unittest.skip("error")
    def test_test(self, data):
        self.success(data)
if __name__ == '__main__':
    unittest.main()
