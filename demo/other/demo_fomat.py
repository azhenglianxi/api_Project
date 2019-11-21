name="tom"
age=20

#1. 输出：你好，tom先生，今晚吃鸡！
print(f"你好，{name}先生，今晚吃鸡！")
print("你好，{}先生，今晚吃鸡！".format(name))

#2. 输出：你好，tom先生，今晚{吃鸡}！
print(f"你好，{name}先生，今晚{{吃鸡}}！")
print("你好，{}先生，今晚{{吃鸡}}！".format(name))

#3. 输出：你好，{tom}先生，今晚吃鸡！
print(f"你好，{{{name}}}先生，今晚吃鸡！")
print("你好，{{{}}}先生，今晚吃鸡！".format(name))


print("姓名和年龄分别是：{}、{}".format(name, age))  # 不带编号,顺序填坑
print("姓名和年龄分别是：{1}、{0}".format(age, name))  # 带数字编号、可以变换顺序
print("姓名和年龄分别是：{x}、{y}".format(x='小明', y=age))  # 带关键字

