#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 10:29 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_15_类方法.py
# @Software: PyCharm
"""


class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性+1
        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        """显示工具计数"""
        print("工具对象总数是 %d 个" % cls.count)


# 1.创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("铁锹")

# 知道使用Tool类创建了多少个对象?
# print("工具对象总数是 %d 个" % tool1.count)
Tool.show_tool_count()