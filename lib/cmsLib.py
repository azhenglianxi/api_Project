import requests
from config import HOST
from lib.loginLib import Login
'''
此模块为cms管理系统模块，目的是给大家演示一下 Token 接口的例子

'''
class CmsManage(Login):
    #1.客户新增
    def add(self,payload):
        try:
            header = {'Content-Type': 'application/json',
                        'X-AUTH-TOKEN':self.Token
                      }
            r=requests.post('http://47.96.181.17:9090/rest/ac01CrmController',
                            json=payload,headers=header
                            )
            # print(r)
            return r.json()
        except:
            return {'code':'1001','message':'服务器错误'}
