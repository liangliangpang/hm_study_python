#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/20 11:15 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_07_父类的私有属性和私有方法.py
# @Software: PyCharm
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))


class B(A):
    def demo(self):
        # 1. 访问父类的私有属性,不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 1. 调用父类的私有方法
        # self.__test()
        pass

# 创建一个子类对象
b = B()
b.demo()
print(b)
