from config import *
payload={
    'action':'add_course',
    'data':'''{
      "name":"初中s22ds大师傅但是",
      "desc":"初中化学课程",
      "display_idx":"4"
    }
    '''
}
#3-2 调用requests的post函数，第一个参数是url，再把字典格式的数据，传递给data
#3-3 根据帮助文档，如果传的是字典格，会字典编码为表单
r=requests.post(f'{HOST}/api/mgr/sq_mgr/',data=payload)
#3-4  文本格式的响应消息体内容，输出
print(r.text)
