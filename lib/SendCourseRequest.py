#!/usr/bin/env python
#@Time     :2019-11-28 15:36:11  
#@Author   :azhenglianxi   

import json
import time

"""
实现功能：传入已登录的课程管理的实例对象和excel中的一行数据，返回请求消息体
传入参数1：CourseManage 已登录的实例对象
传入参数2：row  excel表中的一行数据（字典格式）
"""
def SendCourseRequest(cm,row):
    if (row['调用方法']=='add'):
        # 获取第五列数据，转换为字典
        data =json.loads(row['请求参数'])
        name =data['name']
        name =name.replace('{{courseNanme}}',str(int(time.time())*1000))
        #调用新课程的接口
        dictBody =cm.add(name,data['desc'],data['display_idx'])
        return  dictBody
    if (row['调用方法']=='list'):
        data =json.loads(row['请求参数'])
        dictBody =cm.list(data['pagenum'],data['pagesize'])
        return dictBody
    if (row['调用方法']=='delete'):
        data =json.loads(row['请求参数'])
        dictBody =cm.delete(data['id'])
        return dictBody
    else:
        return {'retcode': '2', 'reason': '暂不实现'}
