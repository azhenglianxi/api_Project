import xlrd
import json
import time
from xlutils.copy import copy
from lib.courseLib import CourseManage

#1-1 打开Excel，获取【workBook】 对象
workBook=xlrd.open_workbook(r'../../data/教管系统-测试用例V1.2.xls',formatting_info=True)

#1-2 从工作簿中，获取【workSheet】对象
workSheet=workBook.sheet_by_index(0)

#2-对象实例化
cm=CourseManage()
cm.login('auto','sdfsdfsdf')

#3-1 复制一个工作簿
workBookNew=copy(workBook)
#3-2 打开工作表
workSheetNew=workBookNew.get_sheet(0)

#1-3 对工作表进行循环
for i in range(1,workSheet.nrows):
    # 1-4 循环中得到具体的一行数据
    row = workSheet.row_values(i)
    #1-5 拿到第1、5、6、7、列的值。
    if row[4]=='add':
        #获取第五列数据，转换为字典
        data=json.loads(row[5])
        name=data['name']#从字典中获取课程名称属性
        #课程名称的变量，用时间戳替换
        name=name.replace('{{courseName}}',str(int(time.time()*1000)))
        #调用课程新增接口
        dictBody = cm.add(name, data['desc'], data['display_idx'])
        # print(dictBody)
        #
        test = json.loads(row[6])
        if (dictBody["retcode"]==test["code"]):
            print(">>>>>测试通过，用例编号：",row[4],row[0])
            workSheetNew.write(i,7,'PASS')
        else:
            print(">>>>>测试不通过，用例编号：",row[4], row[0],dictBody["reason"])
            workSheetNew.write(i, 7, 'FAIL')
            if "reason" in dictBody.keys():
                workSheetNew.write(i, 8, dictBody['reason'])
    elif row[4]=='delete':
        data = json.loads(row[5])
        dictBody = cm.delete(data['id'])
        # print(dictBody)
        test = json.loads(row[6])
        if (dictBody["retcode"] == test["code"]):
            print(">>>>>测试通过，用例编号：",row[4], row[0])
            workSheetNew.write(i, 7, 'PASS')
        else:
            print(">>>>>测试不通过，用例编号：",row[4], row[0])
            workSheetNew.write(i, 7, 'FAIL')
            if "reason" in dictBody.keys():
                workSheetNew.write(i, 8, dictBody['reason'])
    elif row[4]=='list':
        # 获取第五列数据，转换为字典
        data=json.loads(row[5])
        #excel中的参数
        dictBody=cm.list(data["pagenum"],data["pagesize"])

        #获取第七列数据断言
        test=json.loads(row[6])
        if(dictBody["retcode"]==test["code"]):
            print(">>>>>测试通过，用例编号：",row[4], row[0])
            workSheetNew.write(i, 7, 'PASS')
        else:
            print(">>>>>测试不通过，用例编号：",row[4], row[0])
            workSheetNew.write(i, 7, 'FAIL')
            if "reason" in dictBody.keys():
                workSheetNew.write(i, 8, dictBody['reason'])
    elif row[4] == 'modify':
        pass
    else:
        print('未定义：'+row[4])

workBookNew.save(r'../../report/测试结果.xls')
# workBookNew.save(r'C:\Users\Think\Desktop\测试结果2222.xls')
