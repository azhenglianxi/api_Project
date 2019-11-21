from config import *
#2-1 定义一个字典，名字叫payload
payload={
    'action':'list_course',
    'pagenum':1,
    'pagesize':20
}
#2-4 通过params参数，把get的请求参数以字典的格式传递
#2-5 根据帮助文档，params参数会把字典格式转换为表单格式放在url的后面
r=requests.get(f'{HOST}/api/mgr/sq_mgr/',params=payload)
#2-6  文本格式的响应消息体内容，输出
print(r.text)