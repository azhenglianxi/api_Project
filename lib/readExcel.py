#!/usr/bin/env python
#@Time     :2019-11-28 15:35:57  
#@Author   :azhenglianxi   

import xlrd

"""
实现功能：读取excel中的数据，返回一个字典列表
         其中每一行为一个字典，字典的Key为表头，值为字典的内容
传入参数1：fileName 文件名（带路径）
传入参数2：sheetName需要读取的工作表名称
"""

def readExcel(fileName,SheetName="Sheet1"):
    # 1-获取这个工作表
    workBook =xlrd.open_workbook(fileName)
    # 2-得道包内容的第一个sheet 页
    worksheet=workBook.sheet_by_name(SheetName)
    # 3-对【workSheet】工作表进行循环
    nrows =worksheet.nrows
    listData=[]
    if nrows >1 :
        # 1.获取表头内容
        keys = worksheet.row_values(0)
        # 2.对表头下面的数据进行循环
        for i in range(1, nrows):
            row = worksheet.row_values(i)
            # 作用：通过zip和dict 组成字典
            rowDict = dict(zip(keys, row))
            # 3.把字典放入列表中
            listData.append(rowDict)
        return listData
    else:
        return listData


if __name__ == '__main__':
    myData=readExcel('../data/教管系统-测试用例V1.2.xls',"课程管理")
    print(myData)
