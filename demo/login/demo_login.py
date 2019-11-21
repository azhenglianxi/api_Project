from config import *

payload ={"username":"auto","password":"sdfsdfsdf"}
r=requests.post(f'{HOST}/api/mgr/loginReq',data=payload)
print(r.json())
print(r.headers)
print(r.headers['Set-Cookie'])
