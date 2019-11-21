from config import *
payload ={
    'action':'delete_course',
    'id':'1539'
}
r=requests.delete(f'{HOST}/api/mgr/sq_mgr/',data=payload)
print(r.json())