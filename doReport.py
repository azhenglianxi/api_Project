import unittest
from testCase.course.courseTest1 import CourseTest1
from testCase.course.courseTest2 import CourseTest2
import HtmlTestRunner
from HTMLTestRunner import HTMLTestRunner
# 测试套件  test_suite
# 1.-1: 用例 一个个的添加到suite
# suite=unittest.TestSuite()
# suite.addTest(CourseTest1("test_101"))
# suite.addTest(CourseTest1("test_103"))
# suite.addTest(CourseTest1("test_102"))
# suite.addTest(CourseTest1("test_102"))
# suite.addTest(CourseTest2("test_202"))


# 1-2： 用例放入列表中 在添加suite
suite=unittest.TestSuite()
list=[CourseTest1("test_101"),CourseTest1("test_103"),CourseTest1("test_102"),CourseTest2("test_202")]
suite.addTests(list)


# 1-3 :用Testloader类的discover方法来
#suite=unittest.defaultTestLoader.discover('testCase.course',pattern="*Test*.py")

# 2 运行用例，查看结果
# 2-1 第1种情况：不使用HtmlTestRunner插件
# runner=unittest.TextTestRunner()
# runner.run(suite)



# 2-2 第2种情况：使用【经典版】HtmlTestRunner插件
# 新建一个可写二进制文件
# reportFile=open('./report/经典Html报告4.html','wb')
# runner=HTMLTestRunner(stream=reportFile,verbosity=2,description="用例执行详细信息",
#                       title="测试报告")
# runner.run(suite)

# 2-3 第3种情况：使用【最新版】HtmlTestRunner插件
runner=HtmlTestRunner.HTMLTestRunner(output='./report/',report_name='【最新版】html2测试报告',
                                     report_title='my_report')
runner.run(suite)