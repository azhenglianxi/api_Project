import unittest

class CourseTest2(unittest.TestCase):

    #初始化方法（每个测试用例执行前，都会调用逐个方法）
    def setUp(self):
        print('用例执行前初始化')
        pass

    # 初始化方法（每个测试用例执行后，都会调用逐个方法）
    def tearDown(self):
        print('用例执行后清除')
        pass
    # 类级别的（只运行一次）
    @classmethod
    def setUpClass(cls):
        print('所有用例执行前运行一次')

    # 类级别的（只运行一次）
    @classmethod
    def tearDownClass(cls):
        print('所有用例执行后运行一次')

    #测试用例1
    def test_201(self):
        print('执行了测试用例2-1方法')
        '''
        省略
        '''
        self.assertEqual(1, 1, '失败的原因')

    #测试用例3
    def test_203(self):
        print('执行了测试用例2-3方法')
        self.assertEqual(1,1,'失败的原因')

    #测试用例2
    # @unittest.skip('不执行的原因')
    def test_202(self):
        print('执行了测试用例2-2方法')
        self.assertEqual(1, 1, '失败的原因')






