from config import *
payload={
    'action':'modify_course',
    'id':'1539',
    'newdata':'''{
              "name":"初中化学",
              "desc":"初中化学课程",
              "display_idx":"4"
            }
            '''
    }
r=requests.put(f'{HOST}/api/mgr/sq_mgr/',data=payload)
print(r.text)

