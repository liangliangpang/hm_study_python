#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/19 12:17 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_17_私有属性和方法.py
# @Software: PyCharm
"""


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 年龄是 %d" % (self.name, self.__age))


xiaomi = Women("小米")
# 外界无法访问私有属性，但是内部方法可以访问私有属性
# print(xiaomi.__age)
# 外界无法方法私有方法
# xiaomi.__secret()

