from config import *

payload='''
        {
          "action" : "add_course_json",
          "data"	 : {
            "name":"小学数ss学",
            "desc":"sss",
            "display_idx":"4"
          }
        }
        '''
header={'Content-Type':'application/json'}

r=requests.post(f'{HOST}/apijson/mgr/sq_mgr/',data=payload.encode(),headers=header )

print(r.json())