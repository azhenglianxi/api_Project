from config import *
# 新增课程
def add(name,desc,display_idx):
    payload ={
        'action':'add_course',
        'data':f'''{{
           "name":"{name}",
           "desc":"{desc}",
            "display_idx:{display_idx}"
        
            }}
            '''
        }
    r=requests.post(f'{HOST}/api/mgr/sq_mgr/',data=payload)
    return r.json()

#2.列出课程
def list(pagenum,pagesize):
    payload={
        'action':'list_course',
        'pagenum':pagenum,
        'pagesize':pagesize
    }
    r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
    return r.json()

#3.删除课程
def delete(id):
    payload = {
        'action': 'delete_course',
        'id': id
    }
    r = requests.delete(f'{HOST}/api/mgr/sq_mgr/', data=payload)
    return r.json()

#4.修改课程
def modify(name,desc,display_idx):
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
    r = requests.put(f'{HOST}/api/mgr/sq_mgr/', data=payload)
    return r.json()

#新增课程 5
def add2(name,desc,display_idx):
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
    r = requests.post(f'{HOST}/apijson/mgr/sq_mgr/', data=payload.encode(), headers=header)
    print(r.json())