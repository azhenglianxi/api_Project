import unittest
from ddt import ddt,data
from lib.courseLib import CourseManage
import time
import json
from lib.readExcel import readExcel
from lib.SendCourseRequest import SendCourseRequest
myData=readExcel('D:\Program Files\Python_package\Api_Project\data\教管系统-测试用例V1.2.xls',"课程管理")


@ddt
class CourseTest1(unittest.TestCase):
    cm = CourseManage()

    # 类级别的（只运行一次）
    @classmethod

    def setUpClass(cls):
        cls.cm = CourseManage()
        cls.cm.login("auto", "sdfsdfsdf")
        # 数据清除
        cls.clearDate()
        print('begin-所有用例执行前====我调用了\n')
    # 类级别的（只运行一次）
    @classmethod
    def tearDownClass(cls):
        cls.clearDate()
        print('end-所有用例执行后====我调用了')


    #测试用例3【新增一门系统中已经存在的课程，再调用列出课程查看是否存在】
    def test_103(self):
        courseName ='大学语文'+str(int(time.time())*100)
        dictBody =self.cm.add(courseName,'','1')
        self.assertEqual(str(dictBody["retcode"]),'0',"新增不存在的课程失败 了")
        listDate =self.cm.list(1.900)

        dictBody2 = self.cm.add(courseName, "", 1)
        self.assertEqual(str(dictBody2["recode"]), 2)
        listDate2 = self.cm.list(1.900)

        self.assertEqual(listDate, listDate2)
        print("通过测试~")



    # 测试用例2【新增一门系统中不存在的课程，再调用列出课程查看是否存在】
    def test_102(self):

        dictBody =self.cm.add("大学语文"+str(int(time.time()*100)),"",1)
        self.assertEqual(str(dictBody["recode"]),"","新增不存在的课程失败l ")
        listDate =self.cm.list(1,900)  #列出课程 在对列出的课程进行循环

        courseID = dictBody["id"]
        exist = False
        for item in listDate['retlist']:
            if item['id'] == courseID:
                exist = True
                break
        self.assertTrue(exist)
        print("测试通过>>>>")
        self.assertEqual(1, 1, '失败的原因')


    @data(*myData)
    def test_104(self,data):
        print(data)
        #传入excel中的一行数据（字典格式的）---调用函数---返回接口请求体内容
        #self.cm
        resule=SendCourseRequest(self.cm,data)

        #取出excel中的断言这1列，是字符串格式，通过loasd转换为字典格式
        tests = json.loads(data["断言"])

        self.assertEqual(str(resule['retcode']),str(tests['code']))
        print('测试通过')

    def test_101(self):
        print('执行了测试用例2-1方法')
        '''
        省略
        '''
        self.assertEqual(1, 1, '失败的原因')

    @classmethod
    def clearDate(cls):
        # 1.调用列出课程，把所有的课程列出
        listDate = cls.cm.list(1, 900)
        i = 0
        # 2.调用删除课程接口，删除课程
        for course in listDate["retlist"]:
            i = i + 1
            cls.cm.delete(course['id'])
        print('本次共删除数据条数：', i)






