from config import *
class Login:
#用户登录
    def login(self,username,password):
        payload={"username":f"{username}",
                 "password":f"{password}"
                 }
        r=requests.post(f'{HOST}/api/mgr/loginReq',data=payload)
        #  print(r.json())
        #  print(r.cookies['sessionid'])


        #定义一个实例变量(属性)
        self.session_id =r.cookies['sessionid']
        return r.json(),r.cookies['sessionid']
