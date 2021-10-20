#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/16 10:13 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_08___str__方法.py
# @Software: PyCharm
"""


class Cat:
    """这是一个猫类"""

    def __init__(self, new_name):
        self.name = new_name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        return "我是小猫 %s" % self.name


tom = Cat("tom")
print(tom)
