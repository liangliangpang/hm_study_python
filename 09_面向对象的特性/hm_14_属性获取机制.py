# !/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/21 10:00 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_14_属性获取机制.py
# @Software: PyCharm
"""


class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性+1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用Tool类创建了多少个对象?
print("工具对象总数是 %d 个" % tool1.count)
