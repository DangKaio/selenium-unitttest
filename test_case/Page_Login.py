#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-30 15:52:57
# @Last Modified time: 2018-11-10 09:09:21
# @E-mail: 1370465454@qq.com
# @Description:
from time import sleep
import sys
sys.path.append('../')
from common.encapsulation import BasePage


class IndexPage:

    def login(self, username, password):
        # 登录页面
        BasePage.open_url(self,self.base_url)
        BasePage.send_key(self,'css','#username',username)
        BasePage.send_key(self,'css',"#password",password)
        BasePage.click_element(self,"css",".ant-btn")

if __name__ == '__main__':
    login_cookies(self)
