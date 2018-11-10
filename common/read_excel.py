#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dang Kai
# @Date: 2018-11-09 16:47:39
# @Last Modified time: 2018-11-10 08:34:36
# @E-mail: 1370465454@qq.com
# @Description:
import xlrd


class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum - 1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i + 2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == '__main__':
    ExcelUtil = ExcelUtil("../test_data/excel/templet.xlsx", "登录")
    # for data in ExcelUtil.dict_data():
    #     print(data["Action"][action])
    a=ExcelUtil.dict_data()
    print(a[0]["Action"])
    Action = [{'click':"click", 'send_key':"send_key","space": "", 'none':"none", 'skip':"skip", 'js':"js", 'jquery':"jquery"}]
    print(type(Action))
    print(Action[0])
