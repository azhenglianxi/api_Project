import unittest
#import ddt
from lib.courseLib import CourseManage
import time

from lib.courseLib import CourseManage
import time
class TeacherTest3(unittest.TestCase):
    # 类级别的（只运行一次）
    # 初始化 方法（每个测试用例执行前都要调用这个方法）
    def setUp(self):
        print('用例第一步：初始化方法')


    def tearDown(self):
        print('用例最后一步 清楚')
    @classmethod
    def setUpClass(cls): #类级别的变量用例
        print("所有用例执行后运行一次")

    @classmethod
    def tearDownClass(cls):
        print('所有用例执行后运行一次')
     #  测试用例1
    def test_301(self):
        print("执行力测试用例 101")
        self.assertEqual(1,1,'失败的原因')

    def test_303(self):
        print("执行力测试用例 103")
        self.assertEqual(1,1,'失败的原因')
    # 测试用例2
    def test_302(self):
        print("执行力测试用例 102")
        self.assertEqual(1, 1, '失败的原因')
    # @unittest.skip('不执行的原因')

    def test_302(self):
        print('执行了测试用例2-2方法')
        self.assertEqual(1, 1, '失败的原因')
