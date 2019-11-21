from config import *

#用户登录
def login(username,password):
    payload={"username":f"{username}",
             "password":f"{password}"
             }
    r=requests.post(f'{HOST}/api/mgr/loginReq',data=payload)
    print(r.json())
    print(r.cookies['sessionid'])
    return r.json(),r.cookies['sessionid']