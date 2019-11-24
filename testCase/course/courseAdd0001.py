from lib.courseLib import CourseManage
import time

# *****应用层

# 1. 具体实例化课程管理的对象
cm = CourseManage()
cm.login('auto','sdfsdfsdf')
# # 1.用户登录，调用login 函数
# loginBoy,sessionid= loginLib.login('auto','sdfsdfsdf')
# # 2 返回sessionid
# print(sessionid)
# 3，把sessionid 传给课程 新增函数
dictBody=cm.add('大学语文'+str(int(time.time()*100000)),' ','1')
print(dictBody)
if dictBody['retcode']==0:
    print("测试用例执行成功~")