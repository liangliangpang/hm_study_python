#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/19 8:56 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_18_伪私有属性和方法.py
# @Software: PyCharm
"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 年龄是 %d" % (self.name, self.__age))


xiaomi = Women("小米")
# 伪私有属性，在外界不能够被直接访问
print(xiaomi._Women__age)
# 伪私有方法，同样在外界不能够被直接访问
xiaomi._Women__secret()
