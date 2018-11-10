#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-30 15:08:22
# @Last Modified time: 2018-11-10 11:12:59
# @E-mail: 1370465454@qq.com
# @Description: 对selenium的二次封装
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *  # 导入所有的异常类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import os
sys.path.append('../')
from config import globalparam
from common.log import Log
logger = Log()


class BasePage(object):
    original_window = None

    def __init__(self, driver):
        """
            :param driver:打开浏览器驱动
            :param base_url:输入测试url
            :param pagetitle:输入页面title
        """
        self.driver = driver
        self.logger = Log()

    def browser(self, browser="Chrome"):
        """
            打开浏览器函数,Firefox,chrome,IE
            默认Chrome浏览器
        """
        try:
            if browser == "Chrome" or browser == "chrome":
                options = webdriver.ChromeOptions()
                prefs = {'profile.default_content_settings.popups': 0,
                         'download.default_directory': globalparam.download_path}
                options.add_experimental_option('prefs', prefs)
                # cap=webdriver.DesiredCapabilities.CHROME()
                # cap..setglobalparam.download_path
                driver = webdriver.Chrome(
                    chrome_options=options, executable_path=globalparam.driver_path)
                return driver
            elif browser == "Firefox" or browser == "firefox":
                driver = webdriver.Firefox(
                    executable_path=globalparam.driver_path)
                return driver
            elif browser == "IE" or browser == "ie":
                driver = webdriver.Ie(executable_path=globalparam.driver_path)
                return driver
            else:
                logger.error("找不到驱动")
        except Exception as msg:
            logger.error("%s" % msg)

    def getElement(self, *param,timeout=10):
        '''
            根据传入的查找类型查找元素
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
            :timeout:            超时时间设置
            :return:             查找到的元素
        '''
        if param[0] == "id":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.ID, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "class":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.CLASS_NAME, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "name":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.NAME, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "css":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "linktext":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.LINK_TEXT, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "partcialtext":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == "tag":
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.TAG_NAME, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[0]))
        elif param[0] == 'xpath':
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, param[1])))
                return element
            except:
                self.logger.error("查找 %s 元素超时,类型为 %s！！" % (param[1], param[1]))
        elif param[0] == 'js'or param[0] == "jquery":
            return self.ExcuteJs(param[1])
        else:
            self.logger.error("请输入适合的查找元素方式。。。")

    def clear_text(self, *param):
        '''
            输入文本框清空操作
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
        '''
        element = BasePage.getElement(self,param[0], param[1])
        try:
            element.clear()
            self.logger.info('清空文本框内容')
        except NameError as ne:
            self.logger.error("清空文本框内容失败: %s" % ne)
            self.get_screent_img()

    def click_element(self, *param):
        """
            点击某个元素
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
        """

        try:
            element=BasePage.getElement(self,param[0], param[1])
            element.click()
            self.logger.info('成功点击元素 %s: %s...' % (param[0], param[1]))
            time.sleep(2)
        except:
            self.logger.error("无法点击元素 %s: %s..." % (param[0], param[1]))
            raise

    def get_text(self, *param):
        '''
            获取文本
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
        '''
        element = BasePage.getElement(self,param[0], param[1])
        return element.text

    def send_key(self, *param):
        """
            文本框输入内容
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
            :param param[3]:     输入文本的内容

        """

        BasePage.getElement(self,param[0], param[1]).clear()
        self.logger.info('清空%s:%s文本框内容' %(param[0], param[1]))
        time.sleep(1)
        self.logger.info('在 %s:%s在输入内容 %s' % (param[0], param[1],param[2]))
        try:
            BasePage.getElement(self,param[0], param[1]).send_keys(param[2])
            time.sleep(2)
        except Exception as e:
            self.logger.error("在 %s：%s 中输入内容 %s 失败! " % (param[0], param[1], param[2]))

    def move_to_element(self, *param):
        '''
            鼠标悬停操作
            :param param[0]:     查找元素的方式
            :param param[1]:     元素值
            Usage:
            element = ("id","xxx")
            driver.move_to_element(element)
        '''
        element = BasePage.getElement(self,param[0], param[1])
        ActionChains(self.driver).move_to_element(element).perform()

    def close(self):
        """
            关闭浏览器
        """
        try:
            self.driver.close()
            self.logger.info('关闭浏览器窗口')
        except NameError as ne:
            self.logger.error("关闭浏览器窗口失败 %s" % ne)

    def quit(self):
        """
            退出浏览器
        """
        self.driver.quit()

    def browser_back(self):
        """
            浏览器后退
        """
        self.driver.back()

    def browser_forward(self):
        """
            浏览器前进
        """
        self.driver.forward(self)

    def open_url(self, url):
        """
            打开站点
        """
        self.driver.get(url)

    def get_page_title(self):
        '''当前页面title'''
        self.logger.info("当前页面的title为: %s" % self.driver.title)
        return self.driver.title

    def get_screent_img(self):
        '''将页面截图下来'''
        file_path = os.path.dirname(
            os.path.abspath('.')) + globalparam.img_path
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        screen_name = file_path + now + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("页面已截图,截图的路径在项目: %s下" % globalparam.img_path)
        except NameError as ne:
            logger.error("失败截图 %s" % ne)
            self.get_screent_img()




if __name__ == '__main__':
    open_url("")
