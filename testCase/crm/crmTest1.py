import unittest
from ddt import ddt,data
from lib.cmsLib import CmsManage
import random
import json
from lib.readExcel import readExcel
from lib.SendCourseRequest import SendCourseRequest

@ddt
class CrmTest1(unittest.TestCase):

    # 类级别的（只运行一次）
    @classmethod
    def setUpClass(cls):
        cls.cms = CmsManage()
        cls.cms.getToken("fancl", "sq000000")

    #测试用例1【新增客户--token】
    def test_101(self):
        tel = random.randint(1000000,99999999)
        payload={
                "aac003": "麻子",
                "aac004": "1",
                "aac011": "21",
                "aac030": "135"+str(tel),
                "aac01u": "88002255",
                "crm003": "1",
                "crm004": "1",
                "crm00a": "2018-11-11",
                "crm00b": "aaaaaa",
                "crm00c": "2019-02-28",
                "crm00d": "bbbbbb"
            }

        dictBody = self.cms.add(payload)
        self.assertEqual(str(dictBody["code"]), '0000' )

        print('测试通过')
