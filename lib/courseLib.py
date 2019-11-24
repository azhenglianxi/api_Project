from config import *
from lib.loginLib import Login

# 1 定义一个类 叫课程管理
class CourseManage(Login):   # 对象初始化的时候 继承了父类的登录方法

#  **** 子类的课程管理继承父类的login方法

# 好处：子类的实例对象能够调用父类的初始化方案，你能够访问父类的实例变量
# 新增课程
    def add(self,name,desc,display_idx):
        payload ={
            'action':'add_course',
            'data':f'''{{
               "name":"{name}",
               "desc":"{desc}",
                "display_idx":"{display_idx}"
        
                }}
                '''
            }

        # sessionid  需要传给服务器
        cookie ={'sessionid': self.session_id}
        r=requests.post(f'{HOST}/api/mgr/sq_mgr/',data=payload,cookies=cookie)
        return r.json()

    #2.列出课程
    def list(self,pagenum,pagesize):
        payload={
            'action':'list_course',
            'pagenum':pagenum,
            'pagesize':pagesize
        }
        cookie = {'sessionid': self.session_id}
        r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload,cookies =cookie)
        return r.json()

    #3.删除课程
    def delete(self,id):
        payload = {
            'action': 'delete_course',
            'id': id
        }
        cookie = {'sessionid': self.session_id}
        r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', data=payload,cookies= cookie)
        return r.json()

    #4.修改课程
    def modify(self,name,desc,display_idx):
        payload = {
            'action': 'modify_course',
            'id': '1539',
            'newdata': f'''{{
                      "name":"{name}",
                      "desc":"{desc}",
                      "display_idx":"{display_idx}"
                    }}
                    '''
        }
        cookie = {'sessionid': self.session_id}
        r = requests.put(f'{HOST}/api/mgr/sq_mgr/', data=payload,cookies=cookie)
        return r.json()

    #新增课程 5
    def add2(self,name,desc,display_idx):
        payload=f'''
                {{
                  "action" : "add_course_json",
                  "data"	 : {{
                    "name":"{name}",
                    "desc":"{desc}",
                    "display_idx":"{display_idx}"
                  }}
                }}
                '''

        header={'Content-Type':'application/json'}
        cookie = {'sessionid': self.session_id}
        r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', data=payload.encode(), headers=header,cookies=cookie)
        print(r.json())
