import xlrd
import json
import time
from xlutils.copy import copy
from lib.courseLib import CourseManage



# 1-1.打开excel  h获取【workbook】对象
workBook =xlrd.open_workbook('D:\Program Files\Python_package\Api_Project\data\教管系统-测试用例V1.2.xls',formatting_info=True)

# 1-2. 从工作簿里 获【workSheet】对象
workSheet =workBook.sheet_by_index(0)

# 2.对象实例化
cm=CourseManage()
cm.login('auto','sdfsdfsdf')
# 3. 对工作表进行循环  #先获取行数
# 3-1 复制一个工作簿
workBookNew=copy(workBook)
# 3-2 打开工作表
workSheetNew=workBookNew.get_sheet(0)


for i in range(1,workSheet.nrows):
    # 4. 循环中得到具体的一行数据
    row = workSheet.row_values(i)
    # 5. 拿到第 1,5,6,7列的值
    # 增加课程的接口方法
    if row[4]=='add':
     data =json.loads(row[5])     # 将列表转换成为json 格式
     name=data['name']
     name =name.replace('{{courseName}}',str(int(time.time()*1000)))  # 时间戳替换成随机数 吧课程名称
     # 调用课程 新增接口
     dictBody =cm.add(data['name'],data['desc'],data['display_idx'])
    # 取出第6列的数据
     test =json.loads(row[6])
     # 添加断言  code ='0' 是自己添加的
     if (dictBody["retcode"]==test["code"]):
         print("测试用例通过，编号：",row[0],"结果:",row[4])
        # workSheetNew.write(i,7,"pass")
     else:
         print("测试不用例通过，编号：",row[0],row[4])
         workSheetNew.write(i, 7, "FaLL")
        # workSheetNew.write(i, 8, dictBody['reason'])
    # 删除课程的接口方法
    elif row[4]=='delete':
        data =json.loads(row[5])
        dictBody = cm.delete(data['id'])  #删除的话要获取删除的id
        test =json.loads(row[6])
        if (dictBody["retcode"]==test["code"]):
            print("测试用例通过，编号：", row[0],row[4])
            workSheetNew.write(i,7,'PASS')
        else:
            print("测试不用例通过，编号：", row[0],row[4])
            workSheetNew.write(i,7,"FALL")
            # workSheetNew.write(i, 8, dictBody['reason'])
    # 展示列表课程的方法
    elif row[4]=='list':
        data=json.loads(row[5])
        dictBody =cm.list(data["pagenum"],data["pagesize"])  #pagenum  pagesize 【excel】 接口请求参数里规定的

        # 获取第七段的断言
        test = json.loads(row[6])
     # 添加断言  code ='0' 是自己添加的
        if (dictBody["retcode"] == test["code"]):
             print("测试用例通过，编号：", row[0],row[4])
             workSheetNew.write(i, 7, 'PASS')
        else:
            print("测试不用例通过，编号：", row[0],row[4])
            workSheetNew.write(i, 7, 'FALl')
            # workSheetNew.write(i, 8, dictBody['reason'])
    # 其他
    elif row[4] == 'modify':
        pass
    else:
        print('未定义：'+row[4])
workBookNew.save(r'../../report/测试结果.xls')



