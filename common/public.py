#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-10-30 15:09:52
# @Last Modified time: 2018-11-09 14:22:10
# @E-mail: 1370465454@qq.com
# @Description:
import sys
import time
import os
sys.path.append('../')
from config import globalparam
from PIL import ImageGrab

# 截图放到report下的img目录下


def get_img(dr, filename):
    '''对网页进行截图'''
    path = get_path()
    path_filename = path + "\\" + \
        time.strftime('%Y-%m-%d_%H_%M_%S') + filename + '.png'
    dr.save_screenshot(path_filename)


def get_path():
    '''判断目录是否存在，不存在，创建'''
    path = globalparam.img_path + "\\" + \
        time.strftime("%Y-%m-%d", time.localtime(time.time()))
    if os.path.exists(path):
        return path
    else:
        os.makedirs(path)  # 创建文件夹
        return path


def window_screenshoot(filename):
    '''对于有弹窗的用window截图'''
    path = get_path()
    path_filename = path + "\\" + \
        time.strftime('%Y-%m-%d_%H_%M_%S') + filename + '.jpg'
    ImageGrab.grab().save(path_filename)


if __name__ == '__main__':
    get_img(dr, filename)
